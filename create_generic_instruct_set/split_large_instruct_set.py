import json
import random
from pathlib import Path

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_human_gpt_pairs(data):
    pairs = []
    for item in data:
        conversation = item["conversations"]
        pair = {"conversations": []}
        for conv in conversation:
            if conv["from"] in ["human", "gpt"]:
                pair["conversations"].append(conv)
        if len(pair["conversations"]) == 2:
            pairs.append(pair)
    return pairs

def main():
    # Set random seed
    random.seed(42)

    # Load the data
    data = load_json('CleanedOrcaSlimDedup.json')
    pairs = get_human_gpt_pairs(data)

    # Sort pairs by their JSON string length (as a proxy for 'size')
    pairs_sorted = sorted(pairs, key=lambda x: len(x[2]["value"]), reverse=True)

    # Randomize the order of the top 'n' samples
    n = 1000  # Adjust 'n' as needed based on your file size and needs
    top_samples = pairs_sorted[:n]
    random.shuffle(top_samples)

    # Create 3 approximately equal partitions
    part_size = len(top_samples) // 3
    parts = [top_samples[i * part_size:(i + 1) * part_size] for i in range(3)]

    # Add leftover elements to the last partition
    parts[-1].extend(top_samples[3 * part_size:])

    # Save the data to three separate files
    for i, part in enumerate(parts):
        save_json(part, f'output_part_{i+1}.json')

if __name__ == '__main__':
    main()


x[2]["value"]