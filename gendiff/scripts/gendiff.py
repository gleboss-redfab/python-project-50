import argparse
import json


def init_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', dest='format',
                        help='set format of output')

    return parser


def generate_diff(path1, path2):
    # read data
    json1 = json.load(open(path1))
    json2 = json.load(open(path2))

    # get unique keys and sort it
    keys = list(set(json1.keys()) | set(json2.keys()))
    keys.sort()

    # compare and create response
    response = []
    for key in keys:
        if key in json1.keys() and key not in json2.keys():
            response.append(f"- {key}: {json1[key]}")
        elif key in json2.keys() and key not in json1.keys():
            response.append(f"+ {key}: {json2[key]}")
        elif json1[key] != json2[key]:
            response.append(f"- {key}: {json1[key]}")
            response.append(f"+ {key}: {json2[key]}")
        else:
            response.append(f"  {key}: {json1[key]}")

    # print response formated
    print("{")
    for text in response:
        print("  " + text)
    print("}")


def main():
    parser = init_cli_parser()
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
