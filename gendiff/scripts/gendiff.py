import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', dest='format',
                        help='set format of output')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args))
    # print args.


if __name__ == '__main__':
    main()
