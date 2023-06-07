import json

import yaml


def read_data(path1: str, path2: str) -> tuple:
    # check extention and read data
    ext1 = path1.split('.')[-1]
    ext2 = path2.split('.')[-1]
    if ext1 == "json":
        data1 = json.load(open(path1))
    elif ext1 in ["yaml", "yml"]:
        data1 = yaml.load(open(path1), Loader=yaml.BaseLoader)
    else:
        print("Wrong path_1 extention!")
        exit()

    if ext2 == "json":
        data2 = json.load(open(path2))
    elif ext2 in ["yaml", "yml"]:
        data2 = yaml.load(open(path2), Loader=yaml.BaseLoader)
    else:
        print("Wrong path_2 extention!")
        exit()

    return data1, data2


def generate_diff(path1: str, path2: str) -> str | None:
    """Campare 2 json or yaml files and return formated diff
    Args:
        path1 (str): path to 1st file
        path2 (str): path to 1st file
    Returns:
        str: formated diff
    """
    data1, data2 = read_data(path1, path2)

    # get unique keys and sort it
    keys = list(set(data1.keys()) | set(data2.keys()))
    keys.sort()

    # compare and create response
    response = "{\n"
    for key in keys:
        if key in data1.keys() and key not in data2.keys():
            response += f"  - {key}: {str(data1[key]).lower()}\n"
        elif key in data2.keys() and key not in data1.keys():
            response += f"  + {key}: {str(data2[key]).lower()}\n"
        elif data1[key] != data2[key]:
            response += f"  - {key}: {str(data1[key]).lower()}\n"
            response += f"  + {key}: {str(data2[key]).lower()}\n"
        else:
            response += f"    {key}: {data1[key]}\n"

    response += "}"
    return response
