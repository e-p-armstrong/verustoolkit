import os
import json
import yaml

def json_to_yaml(json_dir):
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            json_path = os.path.join(json_dir, filename)
            yaml_path = os.path.join(json_dir, filename[:-5] + ".yaml")

            with open(json_path, "r") as json_file:
                json_data = json.load(json_file)

            with open(yaml_path, "w") as yaml_file:
                yaml.dump(json_data, yaml_file, default_style='"', width=float("inf"), allow_unicode=True)

            # Post-process the YAML file to replace escaped newlines and double escaped quotes
            with open(yaml_path, "r") as yaml_file:
                yaml_content = yaml_file.read()

            yaml_content = yaml_content.replace('\\\\n', '\\n')
            yaml_content = yaml_content.replace('\\\\"', '\\"')

            with open(yaml_path, "w") as yaml_file:
                yaml_file.write(yaml_content)

# Example usage
json_directory = "./prompts"
json_to_yaml(json_directory)