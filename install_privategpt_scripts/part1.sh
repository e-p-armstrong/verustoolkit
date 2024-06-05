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