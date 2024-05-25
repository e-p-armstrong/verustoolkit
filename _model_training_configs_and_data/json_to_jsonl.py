import json
import sys

def convert_json_to_jsonl(input_file, output_file):
    # Open the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)  # Load data from JSON file, assuming it's a list of objects

    # Open the output JSONL file
    with open(output_file, 'w') as f:
        for item in data:
            # Write each JSON object to a single line
            json.dump(item, f)
            f.write('\n')  # Add a newline to separate JSON objects

if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file.json> <output_file.jsonl>")
        sys.exit(1)

    # Assign command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert JSON to JSONL
    convert_json_to_jsonl(input_file, output_file)
