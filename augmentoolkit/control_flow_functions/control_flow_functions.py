import os
import json
import re
import logging
from math import ceil
import traceback
import glob
import uuid
import yaml

from augmentoolkit.utils.escape_unescaped_quotes import escape_unescaped_quotes

from augmentoolkit.generation_functions import (
    extract_question_answer,
    process_multiturn_functions,
)
from augmentoolkit.generation_functions.format_qatuples import format_qatuples

from augmentoolkit.generation_functions.generation_step_class import GenerationStep

with open("./config.yaml", "r") as file:
    obj_conf = yaml.safe_load(file)

DEFAULT_PROMPT_PATH = obj_conf["PATH"]["DEFAULT_PROMPTS"]


def extract_qa_tuples(text):
    pattern = r"\*\*QUESTION:\*\*\s*((?:.|\n)*?)\s*\*\*ANSWER:\*\*\s*((?:.|\n)*?)(?=\s*\*\*QUESTION:\*\*|\Z)"
    matches = re.findall(
        pattern, text + "\n\n**QUESTION:**", re.DOTALL
    )  # The addition is a hack to get around the tricky lookahead problem
    return [(question.strip(), answer.strip()) for question, answer in matches]


def extract_steps(text, steps=[2, 4, 5]):
    """
    Extracts the specified steps from the text.

    Args:
    text (str): The input text containing various steps.
    steps (list of int): The step numbers to extract.

    Returns:
    str: A new string with each specified step's content on its own line.
    """
    step_pattern = "|".join([f"Step {step}\." for step in steps])
    matches = re.findall(
        f"({step_pattern})\s*(.*?)\s*(?=(Step \d\.|$))", text, re.DOTALL
    )

    # Extract and join the matched content, skipping the "Step n." part
    extracted_text = "\n".join(match[1].strip() for match in matches)
    return extracted_text


def extract_first_words(character_name, text):
    # Regular expression pattern to extract first word after the character's name
    pattern = rf"{character_name}: \"(\w+)"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    return matches


import os


# Used basically everywhere:
def make_id():
    return str(uuid.uuid4())


# Also used basically everywhere:
def write_output_to_file(output, directory, uuid):
    # Ensure directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the file path using the directory and UUID
    file_path = os.path.join(directory, f"{uuid}.txt")

    # Write the output to the file
    with open(file_path, "w") as file:
        file.write(output)

    print(f"Output written to {file_path}")


# multiturn helpers
# These will probably be used for multiturn rapid-fire answering.

# Group tuples for multiturn example generation (by chunk of source text) and then run that helper (so that we can make multiturn conversations from questions based on the same paragraphs)
def group_by_text(tuples_list):
    # Dictionary to hold the groups with text as the key
    groups = {}

    # Iterate over each tuple in the list
    for question, answer, text, textname in tuples_list:
        # If the text is not yet a key in the dictionary, add it with an empty list
        if text not in groups:
            groups[text] = []

        print(
            "!!GROUPS COUNT"
        )  # That time I accidentally discovered why the bug is, because I put the print in the for loop by accident. The problem is: some texts have VERY long groups, probably because there's some duplication in the source text.
        print(len(groups))
        # Append the current tuple to the appropriate list
        groups[text].append((question, answer, text, textname))

    # Return the values of the dictionary, which are the lists of tuples grouped by text; also remove duplicates
    return list(groups.values())


def extract_reasoning_from_context_check(response):
    # print("\n----\/----\n RESPONSE:")
    # print(response)
    # print("\n\n\n---/\---\n\n")
    decision_pattern = re.compile(r"Final judgment:(.+)", re.IGNORECASE)
    determination = decision_pattern.search(response)
    if determination:
        determination = determination.group(1).strip()
    if not determination:
        print("Did not contain a determination! MEGA MODEL FAIL LOOK INTO THIS EVAN!!!")
        return None, response
    if "PASS" in determination:
        print("Leaving be...")
        return (True, response)  # , completion
    elif "REWORD" in determination:
        print("Rewording...")
        q, a = extract_question_answer.extract_question_answer(response)
        print((q, a))
        return (q, a)  # (q, a, qatuple[2], qatuple[3]), completion
    elif "FAIL" in determination:
        print("Setting to None...")
        return (False, response)  # , completion
    else:
        print("Did not contain relevant or irrelevant! Retrying")


# Postprocessing function for question/answer validation
async def repair_qatuple_context(
    idx,
    sublist,
    engine_wrapper,
    writepath,
    vetted_qa_tuples,
    completion_mode=None,
    logging_level=logging.INFO,
):
    # NOTE set up the generation step
    context_repairer_path = "check_qatuple_context_no_filenames"
    if completion_mode:
        context_repairer_path = context_repairer_path + ".txt"
    else:
        context_repairer_path = context_repairer_path + ".yaml"

    repair_context_regex = re.compile(
        r"Reasoning and thought process \(be thorough\):(.+)",
        re.DOTALL | re.IGNORECASE,
    )
    context_repairer = GenerationStep(
        prompt_path=context_repairer_path,
        regex=repair_context_regex,
        sampling_params={
            "max_tokens": 2000,
            "stop": [
                "### Response",
                "\n\n\n\n\n\n\n\n\n\n\n\n\n",
                "</s>",
                "# Input:",
                "[INST]",
                "### Instruction",
                "[INST",
                "<|eot_id|>",
                "<|start_header_id|>",
                "<|end_header_id|>",
            ],
            "temperature": 0.2,
        },
        completion_mode=completion_mode,
        retries=1,
        engine_wrapper=engine_wrapper,
        logging_level=logging_level,
        output_processor=extract_reasoning_from_context_check,
        prompt_folder=obj_conf["PATH"]["PROMPTS"],
        default_prompt_folder=DEFAULT_PROMPT_PATH,
        use_stop=obj_conf["SYSTEM"]["STOP"],
    )

    # Resume normal control flow

    # Load files if existing
    existing_files = glob.glob(os.path.join(writepath, f"revised_{idx}_*.json"))

    if len(existing_files) > 0:
        print(f"revised_{idx} Already exists, loading...")
        for file_path in existing_files:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            if content == "failed":
                print("Loaded failed file")
                vetted_qa_tuples[idx] = None
            else:
                try:
                    data = json.loads(content)
                    print("\n\nDATA:")
                    print(data)
                    print("DATA[2]")
                    print(data[2])
                    print("DATA-1:")
                    print(data[-1])
                    print("------/\------\n\n")
                    vetted_qa_tuples[idx] = (data[0], data[1], data[2], data[3])
                except json.JSONDecodeError:
                    print("JSON decode error with the contents:", content)
        return

    # Gen and write files if not existing
    # file_path = os.path.join(writepath, f"revised_{idx}.json")
    # if os.path.exists(file_path):
    #     with open(file_path, "r", encoding="utf-8") as f:
    #         content = f.read()  # Read the file once and store its content
    #         print(file_path)
    #         if content == "failed":
    #             print("Loaded failed file")
    #             vetted_qa_tuples[idx] = None
    #             return None
    #         # print("Loaded file:")
    #         # print(content)
    #         try:
    #             data = json.loads(content)  # Convert the string back to JSON
    #             vetted_qa_tuples[idx] = (data[0], data[1], data[2], data[3])
    #             return None
    #         except json.JSONDecodeError:
    #             print("JSON decode error with the contents:", content)

    for idy, tup in enumerate(sublist):  # idy is the thing after idx, lol
        try:
            revision_id = make_id()
            revision, revision_output = await context_repairer.generate(
                arguments={
                    "textname": tup[3],
                    "question": tup[0],
                    "answer": tup[1],
                }
            )
            write_output_to_file(
                revision_output,
                obj_conf["PATH"]["OUTPUT"] + "/question_context_revision_generations",
                revision_id,
            )  # incidentally, identifying the problem and fixing it in the same step (without another planning step) works a lot better than identifying it and then trying to fix it in the next step.
            if isinstance(revision[0], str):  # if the thing was reworded
                vetted_qa_tuples[idx][idy] = (
                    revision[0],
                    revision[1],
                    tup[2],
                    tup[3],
                )  # replace the old tuple with the new one, revision doesn't have text name so we keep the old one
            elif not revision[0]:
                vetted_qa_tuples[idx][
                    idy
                ] = None  # prepare item for deletion later; right now we just store it as None because indexes
            else:
                pass  # if it passed, we just leave it be and do nothing

            file_path = os.path.join(writepath, f"revised_{idx}_{idy}.json")

            # Write in-progress
            if not os.path.exists(writepath):
                os.makedirs(writepath)

            if vetted_qa_tuples[idx][idy]:
                with open(file_path, "w") as file:
                    json.dump(vetted_qa_tuples[idx][idy], file, indent=4)
            else:
                with open(file_path, "w") as file:
                    file.write("failed")

        except Exception as e:
            print("!!! ERROR!", e)
            traceback.print_exc()


def parse_validation_step(response):
    if "POOR QUALITY" in response:
        return (
            False,
            response,
        )  # TODO ensure that in the control flow code it passes on (False, response), completion
    elif "HIGH QUALITY" in response:
        return (True, response)  # TODO same as above(True, response), completion
    else:
        print("Did not contain relevant or irrelevant! Retrying")
        raise Exception(
            "Validation step screwed up and did not reach a conclusion! Retrying!"
        )


async def vet_quality_loop(
    qa_tuple,
    question_group_id=None,
    engine_wrapper=None,
    double_check_counter=3,
    completion_mode=None,
    logging_level=None,
):
    # NOTE Set up question check generation step
    prompt_path_q_check = "check_quality"
    check_q_regex = re.compile(
        r"Reasoning and thought process:(.+)",
        re.DOTALL | re.IGNORECASE,
    )

    if completion_mode:
        prompt_path_q_check = prompt_path_q_check + ".txt"
    else:
        prompt_path_q_check = prompt_path_q_check + ".yaml"

    question_checker = GenerationStep(
        prompt_path=prompt_path_q_check,
        regex=check_q_regex,
        sampling_params={
            "max_tokens": 1500,
            "stop": [
                "### Response",
                "\n\n\n\n\n",
                "</s>",
                "# Input:",
                "[INST]",
                "### Instruction",
                "[INST",
                "<|eot_id|>",
                "<|start_header_id|>",
                "<|end_header_id|>",
            ],
            "temperature": 0.2,
        },
        completion_mode=completion_mode,
        retries=1,
        engine_wrapper=engine_wrapper,
        logging_level=logging_level,
        output_processor=parse_validation_step,
        prompt_folder=obj_conf["PATH"]["PROMPTS"],
        default_prompt_folder=DEFAULT_PROMPT_PATH,
        use_stop=obj_conf["SYSTEM"]["STOP"],
    )

    # NOTE Set up generate new question step
    # MODIFICATION: so that the conversations make sense, we just toss failed questions, rather than regenning. They're plentiful enough.
    try:
        qtuple = qa_tuple
        # print(
        #     f"\n\nStarting QUESTION loop for question: {qtuple[0]}, context: {qtuple[2]}"
        # )
        run_id = question_group_id + "--subquestion--" + make_id()
        passed_checks = 0
        times_checked = 0
        dissenting_reasoning = ""
        while times_checked < double_check_counter:
            # print(
            #     f"\n\nQUESTION CALL CHECK ANSWER: {qtuple[0]}, context: {qtuple[2]}, retries: {total_retries}, dissenting reasoning: {dissenting_reasoning}"
            # )
            judgement, check_q_output = await question_checker.generate(
                arguments={"text": qtuple[2], "question": qtuple[0]}
            )

            # Now we need to put the judgement together into the format it expects it to be in

            write_output_to_file(
                check_q_output,
                obj_conf["PATH"]["OUTPUT"] + "/check_question_generations",
                run_id,
            )
            if not judgement[0]:  # if not relevant
                dissenting_reasoning = judgement[1]
            else:
                passed_checks += 1
            times_checked += 1
            if passed_checks >= ceil(double_check_counter / 2):
                break
            failed_checks = times_checked - passed_checks
            if failed_checks >= ceil(double_check_counter / 2):
                break

        if passed_checks >= ceil(
            double_check_counter / 2
        ):  # if all question checks passed
            # print(f"\n\nQUESTION CHECKS PASSED retries: {total_retries}")
            return qtuple
        else:
            return (None, None, None, qtuple[3])
    except Exception as e:
        print("!!ERROR!!")
        print(e)
        traceback.print_exc()

    return (None, None, None, qtuple[3])


def parse_answer_accuracy_validation(response):
    if (
        "INACCURATE" in response
    ):  # The "mostly" is there to catch "mostly accurate" which the model says occasionally, and which actually means inaccurate.
        return (False, response)
    elif "ACCURATE" in response:
        return (True, response)
    else:
        print("Answer accuracy validation made a mistake")
        raise Exception("answer accuracy validation did not include a judgement")


# Control flow helpers -- Question/Answer Validation
async def vet_answer_accuracy_loop(
    qa_tuple,
    run_id,
    engine_wrapper=None,
    double_check_counter=3,
    completion_mode=None,
    logging_level=None,
):
    # NOTE Set up answer check generation step
    prompt_path_ans_accuracy_check = "check_answer"
    if completion_mode:
        prompt_path_ans_accuracy_check = prompt_path_ans_accuracy_check + ".txt"
    else:
        prompt_path_ans_accuracy_check = prompt_path_ans_accuracy_check + ".yaml"
    check_ans_accuracy_regex = re.compile(
        r"Reasoning and thought process \(the text is your single source of truth\):\n(.+)",
        re.DOTALL,
    )
    # TODO performance improvement could be gained by using async for to do the checks simultaneously
    answer_accuracy_checker = GenerationStep(
        prompt_path=prompt_path_ans_accuracy_check,
        regex=check_ans_accuracy_regex,
        sampling_params={
            "max_tokens": 1500,
            "stop": [
                "### Response",
                "\n\n\n\n\n",
                "</s>",
                "# Input:",
                "[INST]",
                "### Instruction",
                "[INST",
                "<|eot_id|>",
                "<|start_header_id|>",
                "<|end_header_id|>",
            ],
            "temperature": 0.2,
        },
        completion_mode=completion_mode,
        retries=1,
        engine_wrapper=engine_wrapper,
        logging_level=logging_level,
        output_processor=parse_answer_accuracy_validation,
        prompt_folder=obj_conf["PATH"]["PROMPTS"],
        default_prompt_folder=DEFAULT_PROMPT_PATH,
        use_stop=obj_conf["SYSTEM"]["STOP"],
    )

    # Resume normal control flow code

    try:
        qtuple = qa_tuple
        # print(
        # f"\n\nStarting ACCURACY loop for question: {qtuple[0]}, context: {qtuple[2]}"
        # )
        passed_checks = 0
        times_checked = 0
        dissenting_reasoning = ""
        while times_checked < double_check_counter:
            check_id = make_id()
            # print(
            # f"\n\nACCURACY CALL CHECK ANSWER: {qtuple[0]}, context: {qtuple[2]}, retries: {total_retries}, dissenting reasoning: {dissenting_reasoning}"
            # )
            judgement, answer_accuracy_output = await answer_accuracy_checker.generate(
                arguments={
                    "text": qtuple[2],
                    "question": qtuple[0],
                    "answer": qtuple[1],
                }
            )
            write_output_to_file(
                answer_accuracy_output,
                obj_conf["PATH"]["OUTPUT"] + "/check_answer_accuracy_generations",
                run_id + "--check--" + check_id,
            )
            if not judgement[0]:  # if not accurate
                dissenting_reasoning = judgement[1]
                print("\nNegative Vote Cast! Here was the reasoning:\n")
                print(dissenting_reasoning)
            else:
                passed_checks += 1
            times_checked += 1
            if passed_checks >= ceil(double_check_counter / 2):
                break
            failed_checks = times_checked - passed_checks
            if failed_checks >= ceil(double_check_counter / 2):
                break

        if passed_checks >= ceil(double_check_counter / 2):  # if question checks passed
            # print(f"\n\ANSWER ACCURACY CHECKS PASSED retries: {total_retries}")
            return qtuple
        else:
            print("Answer accuracy validation failed! Tossing")
            return (None, None, None, qtuple[3])
    except Exception as e:
        print("!!ERROR!!")
        print(e)
        traceback.print_exc()

    return (None, None, None, qtuple[3])


def parse_validation_step(response):
    if "IRRELEVANT" in response:
        return (
            False,
            response,
        )  # TODO ensure that in the control flow code it passes on (False, response), completion
    elif "RELEVANT" in response:
        return (True, response)  # TODO same as above(True, response), completion
    else:
        print("Did not contain relevant or irrelevant! Retrying")
        raise Exception(
            "Validation step screwed up and did not reach a conclusion! Retrying!"
        )


async def vet_question_loop(
    qa_tuple,
    question_group_id=None,
    engine_wrapper=None,
    double_check_counter=3,
    completion_mode=None,
    logging_level=None,
):
    # NOTE Set up question check generation step
    prompt_path_q_check = "check_question"
    check_q_regex = re.compile(
        r"Reasoning and thought process \(be careful around \"how\" and \"why\" questions\):(.+)",
        re.DOTALL | re.IGNORECASE,
    )

    if completion_mode:
        prompt_path_q_check = prompt_path_q_check + ".txt"
    else:
        prompt_path_q_check = prompt_path_q_check + ".yaml"

    question_checker = GenerationStep(
        prompt_path=prompt_path_q_check,
        regex=check_q_regex,
        sampling_params={
            "max_tokens": 1500,
            "stop": [
                "### Response",
                "\n\n\n\n\n",
                "</s>",
                "# Input:",
                "[INST]",
                "### Instruction",
                "[INST",
                "<|eot_id|>",
                "<|start_header_id|>",
                "<|end_header_id|>",
            ],
            "temperature": 0.2,
        },
        completion_mode=completion_mode,
        retries=1,
        engine_wrapper=engine_wrapper,
        logging_level=logging_level,
        output_processor=parse_validation_step,
        prompt_folder=obj_conf["PATH"]["PROMPTS"],
        default_prompt_folder=DEFAULT_PROMPT_PATH,
        use_stop=obj_conf["SYSTEM"]["STOP"],
    )

    # NOTE Set up generate new question step
    # MODIFICATION: so that the conversations make sense, we just toss failed questions, rather than regenning. They're plentiful enough.
    try:
        qtuple = qa_tuple
        # print(
        #     f"\n\nStarting QUESTION loop for question: {qtuple[0]}, context: {qtuple[2]}"
        # )
        run_id = question_group_id + "--subquestion--" + make_id()
        passed_checks = 0
        times_checked = 0
        dissenting_reasoning = ""
        while times_checked < double_check_counter:
            check_id = make_id()
            # print(
            #     f"\n\nQUESTION CALL CHECK ANSWER: {qtuple[0]}, context: {qtuple[2]}, retries: {total_retries}, dissenting reasoning: {dissenting_reasoning}"
            # )
            judgement, check_q_output = await question_checker.generate(
                arguments={"text": qtuple[2], "question": qtuple[0]}
            )

            # Now we need to put the judgement together into the format it expects it to be in

            write_output_to_file(
                check_q_output,
                obj_conf["PATH"]["OUTPUT"] + "/check_question_generations",
                run_id + "--check--" + check_id,
            )
            if not judgement[0]:  # if not relevant
                dissenting_reasoning = judgement[1]
                print("\nNegative Vote Cast! Here was the reasoning:\n")
                print(dissenting_reasoning)
                print(f"ID: {check_id}")
            else:
                passed_checks += 1
            times_checked += 1
            if passed_checks >= ceil(double_check_counter / 2):
                break
            failed_checks = times_checked - passed_checks
            if failed_checks >= ceil(double_check_counter / 2):
                break

        if passed_checks >= ceil(
            double_check_counter / 2
        ):  # if all question checks passed
            # print(f"\n\nQUESTION CHECKS PASSED retries: {total_retries}")
            return await vet_answer_accuracy_loop(
                qtuple,
                run_id,
                engine_wrapper=engine_wrapper,
                double_check_counter=double_check_counter,
                completion_mode=completion_mode,
                logging_level=logging_level,
            )
        else:
            print("Question accuracy validation failed! Tossing")
            return (None, None, None, qtuple[3])
    except Exception as e:
        print("!!ERROR!!")
        print(e)
        traceback.print_exc()

    return (None, None, None, qtuple[3])


def extract_questions_from_response_completionmode(
    generation,
):  # TODO extract to non-controlflow file
    questions = extract_qa_tuples(generation)
    if len(questions) == 0:
        print("FAILED TO GENERATE QUESTIONS!")
        return []
    return questions


def extract_questions_from_response_chatmode(
    generation,
):  # TODO extract to non-controlflow file
    questions = extract_qa_tuples(generation)
    if len(questions) == 0:
        print("FAILED TO GENERATE QUESTIONS!")
        return []
    return questions


def extract_question_from_response_completionmode(
    generation,
):  # TODO extract to non-controlflow file
    questions = extract_qa_tuples(generation)
    if len(questions) == 0:
        raise Exception(
            "Failed to generate questions!"
        )  # Because of how the generate step class is structured, this raise will cause a retry, as the original did. No it's not using an exception for normal control flow, if the llm screwed up that's an error.
    return questions[
        0
    ]  # extract only the first question, since we only redo one at a time.


def extract_question_from_response_chatmode(
    generation,
):  # TODO extract to non-controlflow file
    questions = extract_qa_tuples(generation)
    if len(questions) == 0:
        raise Exception(
            "Failed to generate questions!"
        )  # Because of how the generate step class is structured, this raise will cause a retry, as the original did. No it's not using an exception for normal control flow, if the llm screwed up that's an error.
    return questions[
        0
    ]  # we extract only the first question, as we only redo questions one at a time.


# Question generation ASDF
async def generate_qatuples_from_para(
    idx,
    para,
    engine_wrapper=None,
    vetted_qa_tuples=None,
    qa_tuples_dir=None,
    double_check_counter=3,
    completion_mode=None,
    logging_level=None,
):

    question_group = []

    # NOTE Set up qatuple generation step #

    prompt_path_qatuples_gen = "qatuples_gen_no_filenames"

    if completion_mode:
        prompt_path_qatuples_gen = prompt_path_qatuples_gen + ".txt"
    else:
        prompt_path_qatuples_gen = prompt_path_qatuples_gen + ".yaml"

    qatuples_gen_regex = re.compile(
        r"Questions \(make 4\):\n(.+)", re.IGNORECASE | re.DOTALL
    )
    if completion_mode:
        qatuples_generator = GenerationStep(
            prompt_path=prompt_path_qatuples_gen,
            regex=qatuples_gen_regex,
            sampling_params={
                "max_tokens": 2000,
                "stop": [
                    "### Response",
                    "\n\n\n\n\n",
                    "</s>",
                    "# Input:",
                    "[INST]",
                    "### Instruction",
                    "[INST",
                    "<|eot_id|>",
                    "<|start_header_id|>",
                    "<|end_header_id|>",
                ],
                "temperature": 0.8,
                # top_k=-1,
                "top_p": 1,
                # min_p=0.5,
            },
            completion_mode=completion_mode,
            retries=3,
            engine_wrapper=engine_wrapper,
            logging_level=logging_level,
            output_processor=extract_questions_from_response_completionmode,
            prompt_folder=obj_conf["PATH"]["PROMPTS"],
            default_prompt_folder=DEFAULT_PROMPT_PATH,
            use_stop=obj_conf["SYSTEM"]["STOP"],
        )
    else:
        qatuples_generator = GenerationStep(
            prompt_path=prompt_path_qatuples_gen,
            regex=qatuples_gen_regex,
            sampling_params={
                "max_tokens": 2000,
                "stop": [
                    "### Response",
                    "\n\n\n\n\n",
                    "</s>",
                    "# Input:",
                    "[INST]",
                    "### Instruction",
                    "[INST",
                    "<|eot_id|>",
                    "<|start_header_id|>",
                    "<|end_header_id|>",
                ],
                "temperature": 0.8,
                # top_k=-1,
                "top_p": 1,
                # min_p=0.5,
            },
            completion_mode=completion_mode,
            retries=3,
            engine_wrapper=engine_wrapper,
            logging_level=logging_level,
            output_processor=extract_questions_from_response_chatmode,
            prompt_folder=obj_conf["PATH"]["PROMPTS"],
            default_prompt_folder=DEFAULT_PROMPT_PATH,
            use_stop=obj_conf["SYSTEM"]["STOP"],
        )
    # Resume normal control flow code
    try:
        existing_files = glob.glob(
            os.path.join(qa_tuples_dir, f"para_{idx}_*.json")
        )  # check if qs already exist

        if len(existing_files) > 0:  # If files exist, skip this paragraph entirely
            print(f"Skipping para_{idx} as files already exist; loading said files")
            for file_path in existing_files:
                with open(file_path, "r") as file:
                    qa_tuple = tuple(json.load(file))
                question_group.append(qa_tuple)
            vetted_qa_tuples.append(question_group)
            return
        question_group_id = make_id()
        (
            question_answer_tuples,
            question_generation_output,
        ) = await qatuples_generator.generate(
            arguments={
                "text": para[0],
                "textdetails": para[1],
            }
        )

        write_output_to_file(
            question_generation_output,
            obj_conf["PATH"]["OUTPUT"] + "/question_generation_generations",
            question_group_id,
        )
        if not question_answer_tuples:
            print("PARAGRAPH THAT ERRORED:")
            print(para)
            raise Exception(f"{question_group_id} Failed to Generate Questions!")
        question_answer_tuples_more_info = [
            (qatup[0], qatup[1], para[0], para[1]) for qatup in question_answer_tuples
        ]
        for qnum, question_answer_tuple in enumerate(question_answer_tuples_more_info):
            # print(f"\n\n=======!!=BEGIN VETTING QA TUPLE {idx}_{qnum}=!!=======\n\n")
            good_qa_tuple = await vet_question_loop(
                question_answer_tuple,
                question_group_id=question_group_id,
                engine_wrapper=engine_wrapper,
                double_check_counter=double_check_counter,
                completion_mode=completion_mode,
                logging_level=logging_level,
            )

            # Write resulting question file if the tuple is not None
            if good_qa_tuple[0] is not None:
                file_path = os.path.join(qa_tuples_dir, f"para_{idx}_q_{qnum}.json")
                with open(file_path, "w") as file:
                    json.dump(good_qa_tuple, file, indent=4)

            question_group.append(
                good_qa_tuple
            )  # We must filter out all None values at the end; but appending Nones lets us know where things went wrong, and how often.
        vetted_qa_tuples.append(question_group)
    except Exception as e:
        print(f"Q ERROR: {e}")
        traceback.print_exc()


## Paragraph Filtering (worthy for questions?)
async def determine_worthy(
    idx,
    p,
    judged_worthy_for_questions,
    output_dir,
    judge: GenerationStep,
):
    # for idx, p in tqdm(enumerate(paragraphs_processed[:10])):
    file_name = f"{idx}.json"
    file_path = os.path.join(output_dir, file_name)
    # Check if the judgement for this paragraph already exists
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            # print("LOADING: ", data)
        if isinstance(data, str):
            judged_worthy_for_questions.append(
                (None, data[7:])
            )  # hacky way of appending only the text name. See the file output of a failed judgement for details (Takes after "failed|")
        else:
            judged_worthy_for_questions.append((data["paragraph"], data["metadata"]))
    else:
        judgement = await judge.generate(arguments={"text": p[0], "textname": p[1]})
        to_append = (None, p[1])
        if judgement:
            to_append = (p[0], p[1])

        judged_worthy_for_questions.append(to_append)

        # Prepare the data to be written to the file
        if judgement:
            # The paragraph passed the judgement
            data_to_write = {"paragraph": to_append[0], "metadata": to_append[1]}
        else:
            # The paragraph did not pass the judgement
            data_to_write = f"failed|{to_append[1]}"

        # Write the judgement to a unique file as JSON
        with open(file_path, "w") as file:
            json.dump(data_to_write, file)

        # Debug messages
        try:
            if judgement:
                print(f"DEBUG model decided that index {idx} was suitable")
            else:
                print(f"DEBUG model decided that index {idx} was not suitable")
        except:
            print(f"DEBUG max retries exceeded for index {idx}")


def chunking_algorithm(file_path, max_char_length=obj_conf["SYSTEM"]["CHUNK_SIZE"]):
    """
    This function takes a plaintext file and chunks it into paragraphs or sentences if the paragraph exceeds max_char_length.

    :param file_path: Path to the plaintext file
    :param max_char_length: The maximum char5acter length for a chunk
    :return: List of chunks with source text information
    """
    chunks_with_source = []
    current_chunk = []
    char_count = 0
    source_name = file_path.replace(".txt", "")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # try:
    #     with open(file_path, "r", encoding="utf-8") as f:
    #         content = f.read()
    # except Exception as e:
    #     print(f"\nError reading file {file_path}: {e}\n")
    #     return []

    paragraphs = content.split(
        "\n\n"
    )  # Assuming paragraphs are separated by two newlines # TODO change so that if the length is 1 after this, split by tabs instead

    # HOW TO DO IT probably:
    # add tokens to the paragraph until we reach the max length,
    # create chunks out of the remainder of the paragraph (split at max chunk length until it's done)
    # if the final chunk does not have the max length, then make it the new current chunk, set the current token count to its length, and continue with the for loop.

    for paragraph in paragraphs:
        paragraph = paragraph.strip()  # Remove leading and trailing whitespace
        if not paragraph:  # Skip empty paragraphs
            continue

        paragraph_char_count = len(paragraph)

        # Check if the paragraph itself exceeds the max token length
        if paragraph_char_count > max_char_length:

            # Fallback to character chunking for this paragraph
            end_index = (
                max_char_length - char_count
            )  # after this we will take max_char_length chunks starting from end index until the end of the paragraph
            current_chunk.append(paragraph[:end_index])
            # characters = list(paragraph)
            chunks_with_source.append(("".join(current_chunk), source_name))
            current_chunk = []
            while end_index < paragraph_char_count:
                current_chunk.append(paragraph[end_index : end_index + max_char_length])
                chunks_with_source.append(("".join(current_chunk), source_name))
                current_chunk = []
                end_index += max_char_length

            # # handle the remainder of the paragraph
            # end_index = end_index - max_char_length
            # current_chunk.append(paragraph[end_index:])

            # char_count = paragraph_char_count - end_index
        else:
            if char_count + paragraph_char_count <= max_char_length:
                current_chunk.append(paragraph)
                char_count += paragraph_char_count
            else:
                chunks_with_source.append(("".join(current_chunk), source_name))
                current_chunk = [paragraph]
                char_count = paragraph_char_count

    # Add the last chunk if it exists
    if current_chunk:
        chunks_with_source.append(("\n\n".join(current_chunk), source_name))

    return chunks_with_source


def fix_text(to_replace_arr, text):
    for startup in to_replace_arr:
        text = text.replace(startup[0], startup[1])
    return text


async def ensure_multiple_answers_are_same(
    info, conv, multi_turn_conv_generator, completion_mode=None
):  # why is this a whole separate function? Once upon a time, LLMs were used in validation here, too. But programmatic validation SEEMS to catch the common problems. This is here so that I can add it back in if I have to.
    """Loop to ensure that the answer is consistent in the conversation and in the tuple."""
    retries = 0
    c = conv
    while retries < 2:  # try twice, since multiturn is an expensive operation
        if process_multiturn_functions.call_all_processors(
            c[0], info[0]
        ):  # if programmatic validation passes
            return c

        retries += 1
        if retries >= 2:
            return None
        # If we're here, majority of relevance checks failed
        print("----------------\n\n\n\nRETRYING!!!!\n\n\n\n----------------")
        # Broken info is 1) rare and 2) handled by the retry limit. We don't want to waste compute on regenerating info as they take time.
        retry = await make_multiturn_conversation(
            info, multi_turn_conv_generator, completion_mode=completion_mode
        )
        if retry is not None:  # Note: retry CANNOT actually be None
            c = retry
        else:
            # If we failed to generate a retry, don't waste compute
            return None

    return None


async def make_multiturn_conversation(
    info, multi_turn_conv_generator, completion_mode=None
):

    if completion_mode:
        conv, conv_output = await multi_turn_conv_generator.generate(
            arguments={
                "question_answer_list": format_qatuples(info[0]).strip(),
            }
        )
    else:
        conv, conv_output = await multi_turn_conv_generator.generate(
            arguments={
                "question_answer_list": format_qatuples(info[0]),
            }
        )
    write_output_to_file(
        conv_output,
        obj_conf["PATH"]["OUTPUT"] + "/multiturn_conversation_generations",
        info[4],
    )

    return (conv, info[1], info[2], info[3], info[0])


async def create_info(
    idx,
    group,
    multi_turn_convs_info,
    multi_turn_convs_info_dir,
):

    file_path = os.path.join(multi_turn_convs_info_dir, f"info_{idx}.json")

    # Skip if file already exists
    if not os.path.exists(file_path):
        info = (group, "will", "be", "replaced", make_id())

        with open(file_path, "w") as file:
            json.dump(info, file, indent=4)
    else:
        with open(file_path, "r") as file:
            info = json.load(file)

    multi_turn_convs_info.append(
        [info]
    )  # hacky-looking things because the legacy functionality was simplified.


def read_json_files_info(directory):
    # Create a list to hold the tuples
    tuple_list = []

    # Get all the .json files in the directory, sorted
    json_files = sorted([f for f in os.listdir(directory) if f.endswith(".json")])

    # Read each file and convert the contents
    for file in json_files:
        with open(os.path.join(directory, file), "r") as f:
            data = json.load(f)
            # Ensure the data is in the correct format before converting to tuple
            if (
                isinstance(data, list)
                and len(data) == 5
                and isinstance(data[0], list)
                and all(len(item) == 4 for item in data[0])
                and all(isinstance(i, str) for i in data[1:])
            ):
                tuple_list.append((data[0], data[1], data[2], data[3], data[4]))

    return tuple_list


async def create_conversation(
    idx,
    info,
    engine_wrapper,
    multi_turn_convs,
    multi_turn_convs_dir,
    completion_mode=None,
    logging_level=logging.INFO,
):
    file_path = os.path.join(multi_turn_convs_dir, f"conv_{idx}.json")
    multi_turn_conversation_prompt_path = "multi_turn_assistant_conversation"

    conversation_regex = re.compile(
        f"Conversation that answers the provided question \(be sure that you do not change the questions or answers themselves; AI Assistant will answer the questions, not ask them; the questions and answers provided should be copied word for word, and surrounded by compelling conversation\):\n(.+)",
        re.IGNORECASE | re.DOTALL,
    )

    if completion_mode:
        multi_turn_conversation_prompt_path = (
            multi_turn_conversation_prompt_path + ".txt"
        )
    else:
        multi_turn_conversation_prompt_path = (
            multi_turn_conversation_prompt_path + ".yaml"
        )

    multi_turn_conv_generator = GenerationStep(
        prompt_path=multi_turn_conversation_prompt_path,
        regex=conversation_regex,
        sampling_params={
            "max_tokens": 2000,
            "stop": [
                "### Response",
                "\n\n\n\n\n",
                "</s>",
                "# Input:",
                "[INST]",
                "### Instruction",
                "### Information",
                "## Information",
                "## Instruction",
                "Name:",
                "<|eot_id|>",
                "<|start_header_id|>",
                "<|end_header_id|>",
            ],
            "temperature": 0.8,
            # "top_k": -1,
            "top_p": 1,
            # "min_p": 0.6,
        },
        completion_mode=completion_mode,
        retries=1,
        engine_wrapper=engine_wrapper,
        logging_level=logging_level,
        prompt_folder=obj_conf["PATH"]["PROMPTS"],
        default_prompt_folder=DEFAULT_PROMPT_PATH,
        use_stop=obj_conf["SYSTEM"]["STOP"],
    )

    # Skip if file already exists
    if not os.path.exists(file_path):
        try:
            conv = await make_multiturn_conversation(
                info, multi_turn_conv_generator, completion_mode=completion_mode
            )
            final_conv = await ensure_multiple_answers_are_same(
                info, conv, multi_turn_conv_generator, completion_mode=completion_mode
            )

            if final_conv is not None:
                final_conv = (
                    final_conv[0],
                    "AI Assistant",
                    "",
                    "N/A",
                    final_conv[4],
                )
                with open(file_path, "w") as file:
                    json.dump(final_conv, file, indent=4)

            multi_turn_convs.append(final_conv)
        except Exception as e:
            traceback.print_exc()
            print("Had an error, retrying...", e)
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                multi_turn_convs.append(data)
            print(f"Skipped generating {file_path} as it already exists")
        except Exception as e:
            print(f"Error reading {file_path}:", e)
            print("Continuing...")


def convert_directory_to_list(directory_path):
    master_list = []
    simplified_list = []
    simplified_rag_list = []

    for filename in os.listdir(directory_path):  # for each file
        if filename.endswith(".json"):  # if it's a conversation file
            filepath = os.path.join(directory_path, filename)  # get the path
            with open(filepath, "r") as file:  # open it
                try:
                    data = json.load(file)  # load its data
                    if isinstance(data, list) and all(
                        isinstance(item, (list, str))
                        for item in data  # if it has the correct format
                    ):

                        data_dict = {
                            "conversation": data[0],
                            "qa_tuples": [
                                tup[:2] for tup in data[4]
                            ],  # only take first two items from each tuple
                            "rag_context": data[4][0][2],
                            "source_filename": data[4][0][3],
                        }
                        master_list.append(
                            data_dict
                        )  # append it as-is to the master-list

                        # Extract and process conversation
                        conversation, primary_char_desc = (
                            data[0],
                            data[1],
                        )  # first and second items are conv and char desc
                        dialogues = process_multiturn_functions.extract_conversation(
                            conversation
                        )

                        # Convert to simplified format
                        simplified_conversations = []
                        simplified_conversations_rag = []

                        # Load system prompts
                        system_prompt_norag = obj_conf["SYSTEM"][
                            "FINAL_ASSISTANT_PROMPT_NO_RAG"
                        ]
                        system_prompt_rag = obj_conf["SYSTEM"][
                            "FINAL_ASSISTANT_PROMPT_RAG"
                        ]
                        simplified_conversations.append(
                            {"from": "system", "value": system_prompt_norag}
                        )

                        simplified_conversations_rag.append(
                            {
                                "from": "system",
                                "value": system_prompt_rag.replace(
                                    "{data}", data_dict["rag_context"]
                                ),
                            }
                        )
                        for i, (charname, message) in enumerate(
                            dialogues
                        ):  # Skipping the first message
                            from_person = "human" if (i % 2) == 0 else "gpt"
                            simplified_conversations.append(
                                {"from": from_person, "value": f"{message}"}
                            )
                            simplified_conversations_rag.append(
                                {
                                    "from": from_person,
                                    "value": f"{message}",
                                }  # same as above, but for the RAG context
                            )

                        if simplified_conversations:  # If there are any conversations
                            simplified_list.append(
                                {"conversations": simplified_conversations}
                            )
                            simplified_rag_list.append(
                                {"conversations": simplified_conversations_rag}
                            )
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

    # Write the master list to a new .jsonl file
    write_1 = obj_conf["PATH"]["OUTPUT"] + "/master_list.jsonl"
    with open(write_1, "w") as file:
        for item in master_list:
            file.write(json.dumps(item) + "\n")

    # Write the simplified data to a different .jsonl file
    write_2 = obj_conf["PATH"]["OUTPUT"] + "/simplified_data_no_rag.jsonl"
    with open(write_2, "w") as file:
        for item in simplified_list:
            file.write(json.dumps(item) + "\n")

    write_3 = obj_conf["PATH"]["OUTPUT"] + "/simplified_data_rag.jsonl"
    with open(write_3, "w") as file:
        for item in simplified_rag_list:
            file.write(json.dumps(item) + "\n")

    print(
        f"Conversion complete. Master list written to {write_1}. Simplified data written to {write_2} (no RAG) and {write_3} (RAG)."
    )


def convert_directory_and_process_conversations(directory_path):
    master_list = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            filepath = os.path.join(directory_path, filename)
            with open(filepath, "r") as file:
                try:
                    data = json.load(file)

                    if isinstance(data, list) and all(
                        isinstance(item, (list, str)) for item in data
                    ):
                        # Extract and process the conversation part
                        conversations = (
                            process_multiturn_functions.extract_conversation(data[0])
                        )
                        # Convert tuples back to the formatted string as required
                        data[0] = [
                            f"{charname}: {message}"
                            for charname, message in conversations
                        ]
                        master_list.append(data)
                    else:
                        print(f"File {filename} is not in the expected format.")
                except:
                    print(f"Error reading {filename}")

    # Write the master list to a new file
    with open(obj_conf["PATH"]["OUTPUT"] + "/processed_master_list.json", "w") as file:
        json.dump(master_list, file)

    print(
        "Conversion complete. The processed master list is written to 'processed_master_list.json'."
    )


def create_pretraining_set(directory_path, json_file):
    # Initialize a variable to store the combined text of all files
    combined_text = ""

    # Walk through all directories and files in the directory
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Read the contents of the file
            with open(file_path, "r") as file:
                file_contents = file.read()

            # Append the file contents to the combined text, with a separator
            if combined_text:
                combined_text += "\n\n---NEW FILE---\n\n"
            combined_text += file_contents

    # Create a dictionary with the combined text
    data = {"text": combined_text}

    # Save the dictionary as a JSON file
    with open(json_file, "w") as file:
        json.dump(data, file)

    print("JSON file saved successfully.")
