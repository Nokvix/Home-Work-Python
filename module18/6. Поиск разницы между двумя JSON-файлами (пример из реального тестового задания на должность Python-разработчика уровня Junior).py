import json
from typing import Any, Dict, List, Union


def find_value(search_key: str, data: Union[Dict, List]) -> Any:
    if isinstance(data, dict):

        if search_key in data:
            return data[search_key]

        else:
            for key in data.keys():
                if isinstance(data[key], list) or isinstance(data[key], dict):
                    return find_value(search_key, data[key])

    elif isinstance(data, list):
        for elem in data:
            if isinstance(elem, dict) or isinstance(elem, list):
                return find_value(search_key, elem)


def collate_data(old_sample_data, new_sample_data):
    global flag
    if not flag:

        if ((isinstance(old_sample_data, int) and isinstance(new_sample_data, int)) or
                (isinstance(old_sample_data, str) and isinstance(new_sample_data, str))):

            if old_sample_data != new_sample_data:
                flag = True

        else:
            if isinstance(old_sample_data, dict) and isinstance(new_sample_data, dict):
                old_keys = list(old_sample_data.keys())
                new_keys = list(new_sample_data.keys())

                for i in range(len(old_keys)):
                    collate_data(old_sample_data[old_keys[i]], new_sample_data[new_keys[i]])

            elif isinstance(old_sample_data, list) and isinstance(new_sample_data, list):
                min_len = min(len(old_sample_data), len(new_sample_data))

                for index in range(min_len):
                    collate_data(old_sample_data[index], new_sample_data[index])

            else:
                flag = True


diff_list = ["services", "staff", "datetime"]

with open("json_old.json", "r") as file:
    old_data = json.load(file)

with open("json_new.json", "r") as file:
    new_data = json.load(file)

old_sample_data = [find_value(parameters, old_data) for parameters in diff_list]
new_sample_data = [find_value(parameters, new_data) for parameters in diff_list]

result = dict()
flag = False
for i in range(len(diff_list)):
    collate_data(old_sample_data[i], new_sample_data[i])
    if flag:
        if diff_list[i] in result:
            raise KeyError
        else:
            result[diff_list[i]] = new_sample_data[i]
        flag = False

print(result)

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)
