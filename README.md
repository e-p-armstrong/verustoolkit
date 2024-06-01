# Verustoolkit - Train AI To Understand Verus
Verustoolkit is a fork of [Augmentoolkit](https://github.com/e-p-armstrong/augmentoolkit/tree/master) that takes any conceivable written information about the Verus project — websites, API documentation, the vision paper, and more — and turns it into conversational training data for an LLM.

Basically: Verus info goes in, LLM dataset comes out. Train an LLM on that dataset? It *understands* Verus, in a way that RAG cannot achieve.

The Verus project is a privacy-preserving, commerce-enabled, people-powered internet. It is a multi-chain, multi-currency blockchain protocol that is designed to be a platform for the future of the internet. Verustoolkit is designed to help the Verus community train an AI that can answer questions about the Verus project, its technology, and its vision.

This data generation pipeline can be run 100% locally on consumer hardware, ensuring that the Verus community will never be reliant on centralized solutions like OpenAI for producing the data for its chatbots.

## Recommendation: when training on Verustoolkit data, use GaLore to achieve a full finetune, NOT LoRAs.
### (Model training config is provided in repo)

## Demo video
coming soon!

Ready to get started?
## Table of Contents

### Usage
0. [Quickstart](#quickstart)
1. [Installation and Setup](#installation-and-setup)
2. [Customize Settings](#customize-settings)
3. [Training an LLM With your new data](#training-an-llm-with-your-new-data)

### Code Guide (for contributing)
0. [When to Modify the Code](#when-to-modify-the-code)
1. [Important Files](#important-files)
2. [Chatting With Your LLM Using RAG](#chatting-with-your-llm-using-rag)

### Verus
1. [Join the Community!](#join-the-community)
2. [Learn about the Verus project!](#learn-about-the-verus-project)
3. [Have questions? Ask the AI trained to answer them!](#have-questions-ask-the-ai-trained-to-answer-them)


# Usage

## Quickstart
In your favorite terminal, with Python 3.11 installed:
```
git clone https://github.com/e-p-armstrong/verustoolkit.git
cd verustoolkit
pip install -r requirements.txt
python processing.py
```

## Installation and Setup

Verustoolkit is relatively lightweight, foregoing many of the dependencies of the original Augmentoolkit to make contribution easy and development painless.

To run `processing.py` you need only `openai`, `asyncio`, and `aiohttp`.

The other dependencies in `requirements.txt` are for the webui (courtesy of cocktailpeanut, who developed it for the original Augmentoolkit).

Verustoolkit has been tested on Python 3.11.

Once you have a Python environment with 3.11 setup, you can install everything by cloning the repo and installing the requirements.
```
git clone https://github.com/e-p-armstrong/verustoolkit.git
cd verustoolkit
pip install -r requirements.txt
```

Alternatively, you can interact with Augmentoolkit using the WebUI via the following steps:

1. Install the dependencies (pip install -r requirements.txt)
2. Find the absolute path to the `raw_text_input` folder you are using as an input (easy way to do this: `cd` into the raw_text_input folder, then run `pwd`)
3. Run `export GRADIO_TEMP_DIR=<raw_txt_input_absolute_path>`
4. Run `python app.py`
~[](webui.jpeg)

## Customize Settings

You can easily customize how a given run of Verustoolkit proceeds by modifying `config.yaml`. The WebUI also has the ability to customize settings. Let's walk through each field in the YAML file so that you can understand how to change it to suit your needs:

First up, we have the API section:
```
API:
  API_KEY: your key here
  BASE_URL: https://api.together.xyz
  LARGE_LOGICAL_MODEL: meta-llama/Llama-3-70b-chat-hf
  LOGICAL_MODEL: meta-llama/Llama-3-70b-chat-hf
```

Field-by-field:
- `API_KEY` this is where you put the API key for your favorite API provider. If you're running a local server, put a dummy value in here so that the formatting of the request does not break.
- `BASE_URL` this is the base URL for the API provider you are using. Some possible values:
    - http://127.0.0.1:5000/v1/ <- local models.
    - https://api.together.xyz <- together.ai, which offers quality open-source models for cheap prices. Their service has reliability issues sometimes, however.
    - https://api.groq.com/openai/v1 <- Groq. They offer their API for free but have low rate limits.
    - https://api.openai.com/v1/ # <- OpenAI
    - anything else that accepts OAI-style requests, so basically any API out there (openrouter, fireworks, etc...)
- `LARGE_LOGICAL_MODEL` the name of the large model you want to use. This is the model that will be used for the final generation step. This should be a decently-strong model. The model used to power Verustoolkit is separated into two models to save costs on easier steps early on in the pipeline. (This field is likely irrelevant if you're using a local server.)
- `LOGICAL_MODEL` the name of the model you want to use for the first few generation steps. It can be a decently cheap model, but stronger models will still result in better final outputs.

Next up, we have the `PATH` section:

```
PATH:
  INPUT: "./raw_text_input_vision_paper"
  OUTPUT: "./output"
  DEFAULT_PROMPTS: "./prompts"
  PROMPTS: ./prompts_vision_paper
```

Field-by-field:
- `INPUT` the relative path to the folder where the raw text input is stored. This is the folder that contains the text files that you want to use as input to the pipeline. The files can be any format, and some can be nested inside folders if you want, so very little cleanup work is required when working with a new source of data.
- `OUTPUT` the relative path to the folder where the output of the pipeline will be stored. This is the folder that will contain the dataset files (.jsonl) that are generated by the pipeline, as well as a complementary continued-pretraining dataset. Intermediate generations (useful for debugging or interpretability) are also here.
- `DEFAULT_PROMPTS` the relative path to the folder where the core prompts of Verustoolkit are stored. This is the folder that contains the prompt files that are used throughout the pipeline. `DEFAULT_PROMPTS` is the fallback folder that Verustoolkit will use if it can't find a prompt in the `PROMPTS` folder.
- `PROMPTS` the relative path to the folder where the prompts for the current run of Verustoolkit are stored. Compared to `DEFAULT_PROMPTS`, `PROMPTS` is essentially an override: if a prompt is found in the `PROMPTS` folder, it will be used instead of the prompt of the same name in the `DEFAULT_PROMPTS` folder. This allows you to create different prompts for new kinds of input data that the original prompts may not be well-suited for. See `prompts_code_override` and `prompts_vision_paper_override` for examples of how this can be used.

Next, we have the `SYSTEM` section:
```
SYSTEM:
  CHUNK_SIZE: 1900
  COMPLETION_MODE: false
  CONCURRENCY_LIMIT: 60
  DOUBLE_CHECK_COUNTER: 3
  FINAL_ASSISTANT_PROMPT_NO_RAG: You are a crypto expert AI and a member of the Verus
    community, with specialized knowledge about the Verus multi-chain and multi-currency
    blockchain protocol, as well as an understanding of crypto in general. Use your
    knowledge to help questioners understand more about Verus.
  FINAL_ASSISTANT_PROMPT_RAG: 'You are a crypto expert AI and a member of the Verus
    community, with specialized knowledge about the Verus multi-chain and multi-currency
    blockchain protocol, as well as an understanding of crypto in general. Use your
    knowledge and the provided context to help questioners understand more about Verus.
    Context information is below.

    --------------------

    {data}'
  MODE: api
  STOP: true
  SUBSET_SIZE: 10
  USE_SUBSET: true
```

Field-by-field:
- `CHUNK_SIZE` is the maxmimum number of characters to use in a "chunk" of text that will be fed through the pipeline. A chunk is what questions are generated from — it's kinda the core building block of QA datasets built by Verustoolkit.
- `COMPLETION_MODE` is a boolean that determines whether prompts are sent to the provider in chat mode (default, what happens when it's set to `false`) or completion mode (what happens when it's set to `true`). Completion mode can produce higher-quality responses with some models, but many providers don't support it.
- `CONCURRENCY_LIMIT` is an integer; it's the maximum number of concurrent requests that can be made to the provider. This is useful for controlling costs and preventing rate-limiting.
- `DOUBLE_CHECK_COUNTER` is an integer; it's the number of times that the pipeline will double-check the questions it produces. For each QA pair, the majority vote goes: if it's positive, the question/answer pair is kept, if it's negative, the QA pair is tossed. Ties are tossed. This is a tradeoff parameter: higher means more quality but far higher cost. 3 is a good starting point.
- `FINAL_ASSISTANT_PROMPT_NO_RAG` is a setting used to control the form of the dataset produced at the very end. What you write here will be the system prompt of the AI in the portion of the dataset that does NOT have RAG supporting the outputs. This is where we get the LLM to rely on the knowledge we teach it. Recommendation: mention its knowledge of Verus and crypto in general, so that those can be used as "trigger words" for latent space activation when inference time comes.
- `FINAL_ASSISTANT_PROMPT_RAG` is like its NO_RAG cousin, except it's used in the portion of the dataset that DOES have RAG supporting the outputs. This is where we get the LLM to combine understanding with retrieved information to produce an answer. A key difference: wherever `{data}` appears, it will be replaced with the RAG context for each sample in the dataset. So place it where you want the context to appear in the prompt.
- `MODE` is the mode that the pipeline will run in. `api` is the default mode, and is used for running the pipeline with APIs supporting the OpenAI standard. `cohere` is also supported, and is used for running the pipeline with the Cohere API (BASE_URL does nothing in `cohere` mode).
- `STOP` is a boolean that determines whether the pipeline uses stop tokens or not. You should always have this set to `true` unless you're using an API that arbitrarily limits the number of stop tokens you can use, like OpenAI.
- `SUBSET_SIZE` controls the number of chunks fed through the pipeline if USE_SUBSET is on. This is useful for debugging and testing quickly and cheaply — only the first `SUBSET_SIZE` chunks will be processed.
- `USE_SUBSET` is a boolean that determines whether the pipeline uses a subset of the input data.

## Training an LLM With your new data

See the `_model_training_configs_and_data` folder.

TODO demo video -- model training

To train a model on the data produced by Verustoolkit, you can use the provided model training configurations and the data that you generated. The demo video exhaustively shows how to do this, but here's a quick rundown if you have some experience with training LLMs (or CS in general):

1. Rent a GPU instance on a cloud provider like [Vast.ai](https://vast.ai/) or [Runpod](https://www.runpod.io/). If you want to be really secure against Out Of Memory issues, consider using an A100. You can also use a local GPU if you have one. Be sure to use the winglian/axolotl:main-latest docker image.
2. Use SSH to scp the data and model training configuration YAML to the instance's `/workspace/axolotl` folder.
3. If running on a single-GPU setup, you must run: `conda install -c conda-forge mpi4py mpich`
4. Login to HuggingFace with `huggingface-cli login`. On HuggingFace's website, request access to the repo of the base model you are training on if needed (by default, this is `alpindale/Mistral-7B-v0.2-hf`).
5. Then run this command from the `/workspace/axolotl` directory: `accelerate launch --use_deepspeed -m axolotl.cli.train <your config file name>.yaml`. Be sure to replace <your config file name> with the name of the config file you want to use. If you use the provided config file, it would be `config_verus.yaml`.
6. When prompted about whether you want to use weights and biases, pick whatever option you want.
7. Wait for the model to train. This will likely take a couple hours, but unless you're throwing an ungodly amount of data at the problem it will be done in way less than a day.
8. `scp` your model back to your local machine. You can find the model in the `./verus_out` folder on the instance. You'll want all the .safetensors files as well as anything related to the tokenizer. The optimizer and scheduler files are optional -- you only need them if you want to continue training the model later, and they can take a long time to copy over with `scp`. For safety you probably shouldn't delete the instance until you've gotten local inference working with your new model.
9. (optional) for inference, use llama.cpp to convert the model to a less memory-intense format (.gguf). The precise details are on the [Llama.cpp GitHub](https://github.com/ggerganov/llama.cpp), but the gist of it is that first you run `python /path/to/your/llama.cpp/repo/llama.cpp/convert.py <path to your model>` and then run `/path/to/your/llama.cpp/repo/llama.cpp/quantize <path to your model> <output path>.gguf Q8_0`. Change Q8_0 based on what level of quantization you want to use.
10. You can then serve the local LLM file you've created using the text-generation-webui or Ollama. It is recommended to use the former, because Ollama seems to have issues stopping -- it will keep generating text way beyond what is reasonable. When run with the text-generation-webui, the LLM stops at reasonable places most of the time.

## Chatting With Your LLM Using RAG

You need to setup PrivateGPT to use RAG. This is a bit of a process, but it's worth it, as the "grounding" significantly improves the accuracy of the LLM's responses. Here's how you do it:

TODO demo video

# Code Guide (for contributing)

The key parts of Verustoolkit are its code abstractions, and its prompts. The prompts are easy to modify and that's already been covered, but if you need to change a regex, or modify control flow, you'll need to touch code.

This section will start with some common usecases/surgical changes that need to be made, and then will move on to the core structure of the codebase.

## When to Modify the Code

- If you change a prompt radically and are suddenly getting generation failed issues because the Verustoolkit regexes can't parse your new outputs, then you will need to change the Verustoolkit code.
- If you want to add a step to the pipeline, you will need to change the Verustoolkit code.
- If you want to overhaul the Verustoolkit code to use a new API that is not compatible with (or offers additional features compared to) the OpenAI standard, you will need to change the Verustoolkit code.
- If you want to change the sampling parameters of the pipeline, you will need to change the Verustoolkit code.
- If you want to radically overhaul the code in any other way, you will need to change the Verustoolkit code.

## Important Files

Starting from more common things to less common things:

- `processing.py` is the main file that runs the pipeline. It's where the core control flow of the pipeline is defined.
- `control_flow_functions.py` is where a large number of the helper functions that the pipeline uses are defined. Arguments, sampling parameters, and the control flow of each individual step are defined here. The difference between this and `processing.py` is that `processing.py` is the control flow of the pipeline as a whole, while `control_flow_functions.py` is mostly the control flow of each individual step. **This is where the `output processors` are defined -- if you changed prompts and are getting generation failed issues, this is where you need to look.** Look at `parse_validation_step` for an example of what an output processor is like, basically it takes the LLM response as an input and returns a QA pair.
- `engine_wrapper_class.py` contains a class that serves as a single interface for many different LLM APIs. This is where you would need to change the code if you wanted to use a different API provider that is not OpenAI compatible.
- `generation_step_class` contains a class that stores the parameters for a single generation step. Typically you'll change this to add additional logging if you're encountering errors after modifying a step -- the way calls to LLMs work in Augmentoolkit is that a generation step object is created with a path to a prompt and some sampling parameters, and then the object's .generate() method is called with the arguments for a specific call to the LLM. 
- There are some other miscellaneous utility functions in the `generation_functions` folder.
- `app.py` contains the gradio WebUI code. This is the graphic interface. The fields are based off of `config.yaml`.

# Verus

## Join the Community!


[![Discord](https://img.shields.io/badge/chat-Discord-blue?logo=discord)](https://verus.io/discord)

[![Telegram](https://img.shields.io/badge/chat-Telegram-blue?logo=telegram)](https://t.me/veruscommunity)

## Learn about the Verus project!
Interested in a privacy-preserving, commerce-enabled, people-powered internet?

[![Read more about Verus!](https://img.shields.io/badge/-Read%20more%20about%20Verus!-3165D4)](https://verus.io/)


## Have questions? Ask the AI trained to answer them!

[Chat with the custom LLM right now!](https://huggingface.co/VerusCommunity/llama-3-verus-8-epochs-revision-1)

(It will later be available on the Verus Destktop app, where it can run locally.)

If you really want a human to answer your questions,  you can go to the Discord or Telegram links above and ask there. Someone will be happy to help you out.