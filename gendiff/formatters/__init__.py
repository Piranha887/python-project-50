from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import format_json


def format_diff(list_diff, format_name):
    """Formats a list of differences to the specified format. Return string."""
    match format_name:
        case 'stylish':
            return stylish(list_diff)
        case 'plain':
            return plain(list_diff)
        case 'json':
            return format_json(list_diff)
        case _:
            raise ValueError('Format not found!')