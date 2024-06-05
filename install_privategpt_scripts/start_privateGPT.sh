#!/bin/bash

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
  echo "Ollama is not installed. Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
fi

# Open a new terminal window and run `ollama serve`
osascript -e 'tell application "Terminal" to do script "ollama serve"'

# Open another terminal window and run `ollama pull nomic-embed-text`
osascript -e 'tell application "Terminal" to do script "ollama pull nomic-embed-text"'

# Clone the privateGPT repository
git clone https://github.com/imartinez/privateGPT
cd privateGPT

# Download the model file
curl -L -o ggml-model-Q8_0.gguf "https://huggingface.co/VerusCommunity/llama-3-verus-8-epochs-revision-1/resolve/main/ggml-model-Q8_0.gguf"

# Move the model file to the ./models/ directory
mv ggml-model-Q8_0.gguf ./models/

# Check if Python 3.11 is installed
if command -v python3.11 &> /dev/null; then
  # Create a new virtual environment with Python 3.11
  python3.11 -m venv venv
  source venv/bin/activate
else
  echo "Python 3.11 is not installed. Please install it manually or modify the script to use an existing Python version."
  exit 1
fi

# Install llama-cpp-python with Metal support
CMAKE_ARGS="-DLLAMA_METAL=on" pip install --force-reinstall --no-cache-dir llama-cpp-python==0.2.53

# Install additional dependencies
pip install ffmpy==0.3.1
pip install build
pip install poetry
poetry install --extras "ui llms-llama-cpp embeddings-ollama vector-stores-qdrant"
pip install sentencepiece

# Run setup script
poetry run python scripts/setup

# Create the settings-local-and-ollama.yaml file
cat > settings-local-and-ollama.yaml <<EOL
server:
  env_name: \${APP_ENV:local}

llm:
  mode: llamacpp
  max_new_tokens: 512
  context_window: 3900
  tokenizer: Heralax/llama-3-verus
  temperature: 0.3
  min_p: 0.1
  top_p: 0.9
  prompt_style: "tag"

llamacpp:
  llm_hf_repo_id: Heralax/llama-3-verus
  llm_hf_model_file: ggml-model-Q8_0.gguf

embedding:
  mode: ollama

ollama:
  embedding_model: nomic-embed-text
  embedding_api_base: http://localhost:11434
  keep_alive: 5m

vectorstore:
  database: qdrant 

qdrant:
  path: local_data/private_gpt/qdrant
EOL

# Set environment variable and run the application
PGPT_PROFILES=local-and-ollama make run