import json
import yaml
from pathlib import Path


def get_file_extension(path_file):
    """Return the file extension of the given file path"""
    return Path(path_file).suffix


def open_file(path_file, file_extension):
    """Open the file and return the contents as a string"""
    with open(path_file) as f:
        if file_extension.lower() == '.json':
            return json.load(f)
        elif file_extension.lower() == '.yml' or file_extension.lower() == '.yaml':
            return yaml.safe_load(f)


def parse_file(path_file):
    """Parse the file and return the contents as a dictionary"""
    file_extension = get_file_extension(path_file)
    return open_file(path_file, file_extension)
