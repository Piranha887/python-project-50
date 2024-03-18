"""Parsing and open files."""

import argparse


def parser_arg():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    # Change the title of optional arguments
    parser._optionals.title = 'optional arguments'

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
