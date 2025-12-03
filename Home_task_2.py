import random  # Importing random module to generate random numbers
import string  # Importing string module to get letters for dictionary keys

# 1. CREATE A LIST OF RANDOM NUMBER OF DICTS (FROM 2 TO 10)

def generate_numbers_of_dicts() -> int:
    return random.randint(2, 10)


# Generate random number of dictionaries between 2 and 10
# num_dicts = random.randint(2, 10)
# print(num_dicts)

def generate_list_of_dicts(number_of_dicts: int) -> list:

    # Create an empty list to hold our generated dictionaries
    list_of_dicts = []

    # Loop to create each dictionary
    for _ in range(number_of_dicts):
        # Choose a random number of keys for this dictionary (1 to 5)
        num_keys = random.randint(1, 5)

        # Randomly pick letters for dictionary keys
        keys = random.sample(string.ascii_lowercase, num_keys)

        # Create dictionary: each key gets a random value 0–100
        new_dict = {key: random.randint(0, 100) for key in keys}

        # Append this new dictionary to the list
        list_of_dicts.append(new_dict)

    return list_of_dicts


# 2. MERGE ALL DICTS INTO ONE COMMON DICT

def merge_dicts_into_one_dict(list_of_dicts: list) -> dict:

    # Create an empty dictionary where we will store merged values
    merged_dict = {}

    # Loop through all dicts with index (index needed to rename keys)
    for idx, d in enumerate(list_of_dicts, start=1):
        # Loop through each key-value pair in current dictionary
        for key, value in d.items():

            # If the key already exists in merged dict → compare values
            if key in merged_dict:
                # Compare existing value with new one
                if value > merged_dict[key][0]:
                    # Replace value and save new dict index
                    merged_dict[key] = (value, idx)
            else:
                # If key does not exist → store as tuple (value, dict_index)
                merged_dict[key] = (value, idx)

    return merged_dict




def rename_keys_in_dicts(dict_example: dict, list_of_dicts: list) -> dict:

    # Create final dictionary with renamed keys
    final_dict = {}

    # Loop through merged dictionary
    for key, (value, dict_index) in dict_example.items():

        # Count how many dicts had this key
        key_occurrences = sum(key in d for d in list_of_dicts)

        # If key occurred more than once → add suffix "_index"
        if key_occurrences > 1:
            new_key = f"{key}_{dict_index}"
        else:
            new_key = key  # Keep key unchanged

        # Save to final dictionary
        final_dict[new_key] = value

    return final_dict


mun_dicts = generate_numbers_of_dicts()
list_of_dicts = generate_list_of_dicts(mun_dicts)
merged_dict = merge_dicts_into_one_dict(list_of_dicts)
print(rename_keys_in_dicts(merged_dict, list_of_dicts))
