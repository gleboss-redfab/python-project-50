import argparse

from gendiff.gendiff import generate_diff


def init_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', dest='format',
                        help='set format of output')

    return parser


def main():
    parser = init_cli_parser()
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
