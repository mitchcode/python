#!/usr/bin/python3


# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3.3/howto/argparse.html


import configparser
import argparse


TESTING = True


def get_options():
    parser = argparse.ArgumentParser(
        description='simple script to showcase get_options.py',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Example:\n./get_options.py --version=2" + " " +
        '--parameter1="Yes"')
    parser.add_argument("-v", "--version", required=True, action="store",
        help="This is the version. It will store a value from the command line")
    parser.add_argument("--parameter1", required=True, action="store",
        help="This is just some random parameter.")
    args = parser.parse_args()
    return args


def test_print(print_string):
    print("TESTING PRINT: " + print_string)


def main():
    args = get_options()    
    if TESTING is True:
        print("TESTING PRINT: " + args.version)
    if TESTING is True:
        test_print(args.parameter1)


if __name__ == "__main__":
    main()
