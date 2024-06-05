import json
import os
import re

def process_json_file(json_file_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Process each object in the JSON data
    for obj in data:
        title = obj['title']
        latest_published_at = obj['latest_published_at']
        article_url = obj['article_url']
        body_text = obj['body_text']

        # Replace any characters not allowed in filenames with underscores
        cleaned_title = re.sub(r'[<>:"/\\|?*]', '_', title)

        # Create the filename
        filename = f"{cleaned_title}-{latest_published_at}.txt"
        file_path = os.path.join(output_folder, filename)

        # Write the object data to the file
        with open(file_path, 'w') as file:
            file.write(f"Title: {title}\n")
            file.write(f"Article URL: {article_url}\n")
            file.write("Content:\n\n")
            file.write(body_text)

        print(f"Created file: {file_path}")

json_file_path = "medium_veruscoin.json"
output_folder = "medium_text_files"

process_json_file(json_file_path, output_folder)