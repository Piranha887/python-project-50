"""Generating the difference between two files."""
from pathlib import Path

from gendiff.diff_builder import create_diff
from gendiff.formatters.format_diff import format_diff
from gendiff.parse_file import parse_data


def get_file_extension(path_file):
    """Return the file extension of the given file path"""
    return Path(path_file).suffix


def generate_diff(path_file1, path_file2, format_name='stylish'):
    with open(path_file1, 'r') as file1:
        data1 = parse_data(file1, parse_file(path_file1))
    with open(path_file2, 'r') as file2:
        data2 = parse_data(file2, parse_file(path_file2))
    diff = create_diff(data1, data2)
    return format_diff(diff, format_name)


def parse_file(path_file):
    """Parse the file and return the contents as a dictionary"""
    file_extension = get_file_extension(path_file)
    return parse_data(path_file, file_extension)
