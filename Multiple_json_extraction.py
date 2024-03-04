import os
import json
import csv

def print_key_value_pairs(data, prefix="", tags_list=None):
    if tags_list is None:
        tags_list = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                print_key_value_pairs(value, prefix + "." + key, tags_list)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    print_key_value_pairs(item, f"{prefix}.{key}[{i}]", tags_list)
            else:
                tags_list.append((f"{prefix}.{key}", value))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print_key_value_pairs(item, f"{prefix}[{i}]", tags_list)

path_to_json_files = 'clear_capital_jsondata/'
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

with open("clear_capital.csv", "w", newline="", encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Key", "Value", "json_file_name"])
    print("All clear capital data extracted in csv succesfully")
    for json_file_name in json_file_names:
        with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
            json_text = json.load(json_file)
            print_key_value_pairs(json_text, json_file_name)
            tags_list = []
            print_key_value_pairs(json_text, tags_list=tags_list)
            for tag in tags_list:
                writer.writerow([tag[0], tag[1], json_file_name])
