"""Generating the difference between two files."""

from gendiff.parse_file import parse_file
from gendiff.diff import create_diff
from gendiff.formatters.format_diff import format_diff


def generate_diff(path_file1, path_file2, format_name='stylish'):
    """Create a difference between two files in a selected format.
    Return string."""
    dict1 = parse_file(path_file1)
    dict2 = parse_file(path_file2)
    list_diff = create_diff(dict1, dict2)
    return format_diff(list_diff, format_name)
