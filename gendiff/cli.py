import argparse
from gendiff.constants import STYLE_FORMAT_CHOICES


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
        prog='gendiff'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=STYLE_FORMAT_CHOICES,
                        help='select format of output')

    return parser.parse_args()
