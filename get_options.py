#!/usr/bin/python3

import configparser
import argparse

TESTING = True

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", required=True, action="store",
        help="This is the version. It will store a value from the command line")
    args = parser.parse_args()
    return args

def main():
    args = get_options()
    
    if TESTING is True:
        print("TESTING PRINT: " + args.version)

if __name__ == "__main__":
    main()
