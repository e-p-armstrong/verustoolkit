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

def partition_data(pairs, limit_mb=4):
    limit_bytes = limit_mb * 1024 * 1024  # MB to bytes
    partitions = [[], [], []]
    current_partition = 0
    current_size = 0
    
    for pair in pairs:
        pair_size = len(json.dumps(pair).encode('utf-8'))
        if current_size + pair_size > limit_bytes:
            current_partition += 1
            current_size = 0
            if current_partition > 2:  # Only three partitions allowed
                break
        partitions[current_partition].append(pair)
        current_size += pair_size
    
    return partitions

def main():
    # Set random seed
    random.seed(42)

    # Load the data
    data = load_json('CleanedOrcaSlimDedup.json')
    pairs = get_human_gpt_pairs(data)

    # Sort pairs by their JSON string length (as a proxy for 'size')
    pairs_sorted = sorted(pairs, key=lambda x: len(json.dumps(x)), reverse=True)

    # Shuffle to avoid any ordering biases
    random.shuffle(pairs_sorted)

    # Partition the data
    partitions = partition_data(pairs_sorted)

    # Save the data to three separate files
    for i, part in enumerate(partitions):
        save_json(part, f'output_part_{i+1}.json')

if __name__ == '__main__':
    main()
