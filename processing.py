import asyncio

# created with nbconvert, minimally cleaned up


async def main():
    # NOTE NOTEBOOK SETTINGS AND CONSTANTS (some script file constants are in generation_functions/constants.py)

    # Put your desired quant of your desired model in the relevant directories

    import logging
    import yaml
    import glob

    with open("./config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # "airoboros-l2-70b-3.1.2.Q4_K_M.gguf" <- recommended for the large logical model
    # "flatorcamaid-13b-v0.2.Q8_0.gguf" <- recommended for the normal logical model
    # A6000s on Vast.ai are a good choice for running this notebook

    if (
        not config["SYSTEM"]["COMPLETION_MODE"]
        and config["SYSTEM"]["MODE"] == "aphrodite"
    ):
        raise Exception("Aphrodite engine mode MUST use completion prompts!")

    LOGICAL_MODEL = config["API"]["LOGICAL_MODEL"]

    LARGE_LOGICAL_MODEL = config["API"]["LARGE_LOGICAL_MODEL"]

    ASSISTANT_MODE = config["SYSTEM"][
        "ASSISTANT_MODE"
    ]  # change to true if you want all conversations to be with an "AI language model" and not characters. Useful for more professional use cases.

    DOUBLE_CHECK_COUNTER = config["SYSTEM"][
        "DOUBLE_CHECK_COUNTER"
    ]  # Set to 1 to check outputs only once; set to 2 to check twice; set to 3 to check thrice, etc. Set to 0 to break everything in vet_question_loop() and elsewhere. Set to -1 and cause the universe to implode?

    USE_SUBSET = config["SYSTEM"][
        "USE_SUBSET"
    ]  # Set to True if you want to use only a small subset of the text, to test whether it plays nicely with the current setup of the notebook

    REARRANGEMENTS_TO_TAKE = config["SYSTEM"][
        "REARRANGEMENTS_TO_TAKE"
    ]  # How many of the possible permutations of tuples in a group to take and make multiturn convs out of. Adjust higher to get more data out of less text, but it might be a bit repetitive. NOTE your eval loss will be basically worthless if you aren't careful with how you shuffle your dataset when you're about to train.

    USE_FILENAMES = config["SYSTEM"][
        "USE_FILENAMES"
    ]  # Turn on if you want the model to use the names of your files as additional context (this is what original Augmentoolkit does). Useful if you have a small number of large input files grouped by subject matter, IE books. Turn off if you have a large number of files with meaningless names.

    CONCURRENCY_LIMIT = config["SYSTEM"][
        "CONCURRENCY_LIMIT"
    ]  # Adjust this number based on the rate limit constraints of your api

    API_KEY = config["API"]["API_KEY"]

    BASE_URL = config["API"][
        "BASE_URL"
    ]  # Augmentoolkit-API should also be compatible with any other API provider that accepts OAI-style requests

    COMPLETION_MODE = config["SYSTEM"]["COMPLETION_MODE"]

    MODE = config["SYSTEM"]["MODE"]

    LOG_LEVEL = logging.INFO

    INPUT_FOLDER = config["PATH"]["INPUT"]

    # extension = ".md"

    path = f"{INPUT_FOLDER}/*"# + extension
    source_texts = glob.glob(path)

    print(source_texts)

    # [ # add your texts here
    #     "./raw_txt_input/Simple Sabotage, by the Office of Strategic Services, published 1944.txt",
    # ]

    # ## Below: Defines and imports functions that you will probably use no matter what cells in the script you choose to run:

    print(
        "\n\n\nIMPORTANT NOTE! Augmentoolkit prints a lot of stuff when it runs. Including tracebacks caused by model errors. Most errors are the result of the models, not the code, and any tracebacks you see were almost certainly handled. So: don't panic! You're gonna make it! Alright that's the end of this PSA. Happy dataset generation!\n\n\n"
    )

    import os
    import uuid

    # This is in no way best practices, but all my prompts being searchable and separate files is a good way to make my life easier.
    import pkgutil
    import importlib
    import sys
    from tqdm import asyncio as tqdmasyncio
    import asyncio

    # Set up rate-limit-conscious functions
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async def run_task_with_limit(task):
        async with semaphore:
            # Run your task here
            return await task

    # We have to define this up here so that two-step generation works, you'll see later.
    multi_turn_convs_info_dir = (
        config["PATH"]["OUTPUT"] + "/multi_turn_convs_info"
    )  # we generate all the information fed to the multiturn prompt, and generate the actual multiturn prompt, separately; since every step but the last is capable of being done by a 13b

    sys.path.append("./generation_functions")
    sys.path.append("./control_flow_functions")

    import augmentoolkit.generation_functions as generation_functions  # This is the package directory
    from augmentoolkit.control_flow_functions import control_flow_functions
    from augmentoolkit.generation_functions.engine_wrapper_class import EngineWrapper

    # First, import all modules so they can be reloaded
    for _, module_name, _ in pkgutil.iter_modules(
        generation_functions.__path__, generation_functions.__name__ + "."
    ):
        importlib.import_module(module_name)

    # Now, reload each module and import all callable attributes
    for _, module_name, _ in pkgutil.iter_modules(
        generation_functions.__path__, generation_functions.__name__ + "."
    ):
        # Reload the module
        module = importlib.reload(sys.modules[module_name])
        # Iterate through each attribute in the reloaded module
        for attribute_name in dir(module):
            # Retrieve the attribute
            attribute = getattr(module, attribute_name)
            if callable(attribute):
                # If it's callable, it's a function or class, so you set it in the globals dictionary
                globals()[attribute_name] = attribute

    engine_wrapper = EngineWrapper(
        model=LOGICAL_MODEL,
        api_key=API_KEY,
        base_url=BASE_URL,
        mode=MODE,
        # quantization="gptq" # modify if you want to do stuff with the aphrodite branch
    )

    import re
    from tqdm import tqdm
    import pprint

    sentence_chunks = []
    print("Chunking text...")
    for source_text in source_texts:
        sentence_chunks += control_flow_functions.chunking_algorithm(
            source_text
        )

    conversions = [("  ", " ")]

    paragraphs_processed = [
        (control_flow_functions.fix_text(conversions, seq[0]), seq[1])
        for seq in sentence_chunks
    ]
    
    pprint.pprint(paragraphs_processed[:5])

    import json
    import os
    from tqdm import tqdm
    import asyncio

    # Create directory if it doesn't exist
    output_dir = config["PATH"]["OUTPUT"] + "/worthy_for_questions"
    os.makedirs(output_dir, exist_ok=True)

    filtered_worthy_for_questions = paragraphs_processed
    if USE_SUBSET:
        filtered_worthy_for_questions = filtered_worthy_for_questions[:config["SYSTEM"]["SUBSET_SIZE"]]
    # ### The cell below begins generating questions. SOME OF THESE MAY FAIL and have to retry due to model errors (the API branch cannot use grammars). But if you let it run you will see that the vast majority eventually get through.

    # control flow
    import json
    import os
    import glob

    # Directory for QA tuples
    qa_tuples_dir = config["PATH"]["OUTPUT"] + "/qatuples_raw"
    if not os.path.exists(qa_tuples_dir):
        os.makedirs(qa_tuples_dir)

    # save the filtered_worthy_for_questions to a file
    with open(
        config["PATH"]["OUTPUT"] + "/filtered_worthy_for_questions.json", "w"
    ) as f:
        json.dump(filtered_worthy_for_questions, f)

    vetted_qa_tuples = []  # tuple list of qa tuples that have been judged good

    # Attempt to initialize filtered_worthy_for_questions

    tasks = [
        control_flow_functions.generate_qatuples_from_para(
            idx,
            para,
            engine_wrapper=engine_wrapper,
            vetted_qa_tuples=vetted_qa_tuples,
            qa_tuples_dir=qa_tuples_dir,
            double_check_counter=DOUBLE_CHECK_COUNTER,
            use_filenames=USE_FILENAMES,
            completion_mode=COMPLETION_MODE,
            logging_level=LOG_LEVEL,
        )
        for idx, para in enumerate(filtered_worthy_for_questions)
    ]
    limited_tasks_qgen = [run_task_with_limit(task) for task in tasks]
    for future in tqdmasyncio.tqdm.as_completed(limited_tasks_qgen):
        await future

    print(
    "-------------- QUESTIONS CREATED ------------- STATS SO FAR (may be wrong if run was continued from interruption):"
    )
    total_nones = 0
    total_non_nones = 0
    filtered_vetted_qa_tuples = []

    # first filter out None sublists:
        

    for sublist in vetted_qa_tuples:
        filtered_sublist = [qa for qa in sublist if qa is not None]
        if filtered_sublist:
            filtered_vetted_qa_tuples.append(filtered_sublist)
            total_nones += len(sublist) - len(filtered_sublist)
            total_non_nones += len(filtered_sublist)

    print(f"Nones: {total_nones}")
    print(f"Non-nones: {total_non_nones}")
    print(f"Total: {total_nones + total_non_nones}")
    print("---------------- ONTO EXAMPLES GENERATION-------------------")

    # print(vetted_qa_tuples)
    filtered_vetted_qa_tuples
    # Check for and fix the common mistake: mentioning "the text".
    writepath = config["PATH"]["OUTPUT"] + "/qatuples_revised"
    import json

    # TODO turn repairing context into a "link removal" and other cleanup function
    # And add the step back
    
    
    
    # HERE WE GROUP THE QUESTIONS BY PARAGRAPH IN A DICT WHERE THE KEY IS THE PARA NUMBER (like para_0, para_1, etc. from the previous step)
    
    # TODO
    
    
    
    
    ##### QATUPLES REPAIR (modify so that it iterates over the paragraph groups and calls repair on each question in each group, writing to files prefixed by para_x_q_y depending on the idx or key of the group and the idx of the question in the group) instead of just going over all questions and relying on distinct texts.
    # This next step will also create groups, we don't need to group_by_text that will go away, we create and append to the groups as we revise the questions. That way it is compatible with the rest of the steps.
    
    # Check for and fix the common mistake: mentioning "the text".
    writepath = config["PATH"]["OUTPUT"] + "/qatuples_revised"
    import json

    # Assuming vetted_qa_tuples is a list that might or might not exist

    # Load all files at the start if vetted_qa_tuples is empty
    tasks = [
        control_flow_functions.repair_qatuple_context(
            idx,
            sublist,
            engine_wrapper,
            writepath,
            filtered_vetted_qa_tuples,
            completion_mode=COMPLETION_MODE,
        )
        for idx, sublist in enumerate(filtered_vetted_qa_tuples)
    ]
    limited_tasks_qcorrection = [run_task_with_limit(task) for task in tasks]
    for future in tqdmasyncio.tqdm.as_completed(limited_tasks_qcorrection):
        await future

    # Print stats related to revised qatuples, and filter out nones (questions that were unanswerable due to lack of context).
    import json
    import os

    print("-------------- QUESTIONS REVISED ------------- STATS SO FAR:")
    total_nones = 0
    total_non_nones = 0
    revised_filtered_vetted_qa_tuples = []

    for sublist in filtered_vetted_qa_tuples:
        filtered_sublist = [qa for qa in sublist if qa is not None]
        if filtered_sublist:
            revised_filtered_vetted_qa_tuples.append(filtered_sublist)
            total_nones += len(sublist) - len(filtered_sublist)
            total_non_nones += len(filtered_sublist)

    print(f"Nones: {total_nones}")
    print(f"Non-nones: {total_non_nones}")
    print(f"Total: {total_nones + total_non_nones}")
    print("---------------- ONTO EXAMPLES GENERATION-------------------")

    ##### QATUPLES REPAIR

    # Safe to delete the stuff below until the next comment about deletion ONCE THE ABOVE IS WORKING

    import os

    if not os.path.exists(multi_turn_convs_info_dir):
        os.makedirs(multi_turn_convs_info_dir)

    import json
    import random
    import itertools

    multi_turn_convs_info = []

    tasks = [
        control_flow_functions.create_info(
            idx,
            group,
            multi_turn_convs_info,
            multi_turn_convs_info_dir,
        )
        for idx, group in enumerate(revised_filtered_vetted_qa_tuples)
    ]
    limited_tasks_infocreation = [run_task_with_limit(task) for task in tasks]
    for future in tqdmasyncio.tqdm.as_completed(limited_tasks_infocreation):
        await future
    # You can safely delete the stuff above until the other comment about deletion

    engine_wrapper = EngineWrapper(
        model=LARGE_LOGICAL_MODEL,
        api_key=API_KEY,
        base_url=BASE_URL,
        mode=MODE,
    )

    import os
    import json

    convs_info = control_flow_functions.read_json_files_info(multi_turn_convs_info_dir)

    import os
    import json
    import random
    import itertools
    import asyncio

    multi_turn_convs_dir = config["PATH"]["OUTPUT"] + "/multi_turn_convs"
    if not os.path.exists(multi_turn_convs_dir):
        os.makedirs(multi_turn_convs_dir)

    multi_turn_convs = []

    tasks = [
        control_flow_functions.create_conversation(
            idx,
            info,
            engine_wrapper,
            multi_turn_convs,
            multi_turn_convs_dir,
            assistant_mode=ASSISTANT_MODE,
            completion_mode=COMPLETION_MODE,
            logging_level=LOG_LEVEL,
        )
        for idx, info in enumerate(convs_info)
    ]
    limited_tasks_convwriting = [run_task_with_limit(task) for task in tasks]
    for future in tqdmasyncio.tqdm.as_completed(limited_tasks_convwriting):
        await future

    # # Yay! Now you have a dataset!

    import os
    import json

    # Make ShareGPT-format dataset (I think, still need verification it actually works)
    control_flow_functions.convert_directory_to_list(
        config["PATH"]["OUTPUT"] + "/multi_turn_convs/"
    )
    # Make dataset in a format that has all the information. See README for details on this format.
    control_flow_functions.convert_directory_and_process_conversations(
        config["PATH"]["OUTPUT"] + "/multi_turn_convs/"
    )

    with open(config["PATH"]["OUTPUT"] + "/processed_master_list.json", "r") as f:
        first = f.read()
        data = json.loads(first)

    # For curiosity's sake, you can find out how many lines of dialogue you generated
    def filter_and_flatten(lst):
        flat_list = []

        # Loop through each sublist in the main list
        for sublst in lst:
            # Check if the first element of the sublist is itself a list (subsublist1)
            if isinstance(sublst[0], list):
                # Extend the flat_list with the elements from subsublist1
                flat_list.extend(sublst[0])

        return flat_list

    len(filter_and_flatten(data))


asyncio.run(main())
