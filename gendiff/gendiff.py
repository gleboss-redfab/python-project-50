import json


def generate_diff(path1: str, path2: str) -> str:
    """Campare 2 json files and return formated diff

    Args:
        path1 (str): path to 1st JSON
        path2 (str): path to 1st JSON

    Returns:
        str: formated diff
    """
    # read data
    json1 = json.load(open(path1))
    json2 = json.load(open(path2))

    # get unique keys and sort it
    keys = list(set(json1.keys()) | set(json2.keys()))
    keys.sort()

    # compare and create response
    response = "{\n"
    for key in keys:
        if key in json1.keys() and key not in json2.keys():
            response += f"  - {key}: {json1[key]}\n"
        elif key in json2.keys() and key not in json1.keys():
            response += f"  + {key}: {json2[key]}\n"
        elif json1[key] != json2[key]:
            response += f"  - {key}: {json1[key]}\n"
            response += f"  + {key}: {json2[key]}\n"
        else:
            response += f"    {key}: {json1[key]}\n"

    response += "}"
    return response
