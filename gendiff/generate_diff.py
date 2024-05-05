from gendiff.parse_file import parse_data
from gendiff.constants import DATA_FORMAT_CHOICES, STYLE_FORMAT_CHOICES
from gendiff.formatters import format_diff
from gendiff.diff_builder import create_difference_tree
import os


def define_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()[1:]
    match extension:
        case 'json':
            return DATA_FORMAT_CHOICES.JSON
        case 'yaml' | 'yml':
            return DATA_FORMAT_CHOICES.YAML
        case _:
            raise ValueError(
                f'Unsupported extension: {extension}'
            )


def get_file_data(file_path):
    data_format = define_file_extension(file_path)
    with open(file_path) as file:
        data = file.read()
        return parse_data(data, data_format)


def generate_diff(file_path1, file_path2, formatter=STYLE_FORMAT_CHOICES.STYLISH):
    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)
    diff = create_difference_tree(data1, data2)
    return format_diff(diff, formatter)
