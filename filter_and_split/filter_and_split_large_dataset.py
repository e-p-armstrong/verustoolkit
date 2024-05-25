

import json
import random


def read_and_sort_data(file_path: str) -> list:
    with open(file_path, 'r') as file:
        data = file.read()
        json_data = json.loads(data)
    sorted_json_data = sorted(json_data, key=lambda x: len(x["conversations"][2]["value"]), reverse=True)
    
    
    return sorted_json_data


def take_megabytes_of_data(sorted_json_data: list, megabytes: int) -> list:
    """Takes the first n megabytes of data from the sorted json data. Megabytes are counted by the length of the value string across all elements of each sublist (sorted json data is a list of sublists of objects with a "value" key that is a string).

    Args:
        sorted_json_data (list)
        megabytes (int)

    Returns:
        list:
    """
    
    # Each byte is 1 character
    max_chars = megabytes * 1024 * 1024
    
    total_chars = 0
    
    taken = []
    
    # filter out any data that is too short
    
    # sum the length of the value strings of everything from index 0 to index 2 until the max chars is reached
    for sublist in sorted_json_data:
        if total_chars + sum([len(i["value"]) for i in sublist["conversations"]]) <= max_chars:
            taken.append(sublist)
            total_chars += len(sublist["conversations"][2]["value"])
        else:
            break
    
    # Shuffle the data
    random.shuffle(taken)
    
    # split taken into 3 lists
    split = [taken[i:i + len(taken) // 3] for i in range(0, len(taken), len(taken) // 3)]
    
    return split

if __name__ == "__main__":
    sorted_json_data = read_and_sort_data("orca_slim_dedup_cgato.json")
    split_data = take_megabytes_of_data(sorted_json_data, 12)
    
    # Write each split to a file
    for i, data in enumerate(split_data):
        with open(f"split_data_{i}.json", 'w') as file:
            json.dump(data, file)