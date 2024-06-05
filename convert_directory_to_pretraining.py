import json
import os
import argparse

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Process files into a single JSON.')
parser.add_argument('--directory', type=str, default='./raw_text_input_docs',
                    help='Directory containing the text files')
parser.add_argument('--output', type=str, default='pretraining_vision.json',
                    help='Output JSON file name')
args = parser.parse_args()

# Specify the directory containing the files
directory_path = args.directory

# Specify the path to save the JSON file
json_file = args.output

# Initialize a variable to store the combined text of all files
combined_text = ""

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Check if the current file is a file (and not a directory, etc.)
    if os.path.isfile(file_path):
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

print(f"JSON file '{json_file}' saved successfully.")
