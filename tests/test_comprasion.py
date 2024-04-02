"""Test generate_diff"""

import pytest
from gendiff.generate_diff import generate_diff
from pathlib import Path


@pytest.mark.parametrize(
    "file1,file2,right_answer_stylish,right_answer_plain,right_answer_json",
    [
        ('file1.json', 'file2.json', 'right_answer_stylish.txt', 'right_answer_plain.txt', 'right_answer_json.json'),
        ('file1.yml', 'file2.yml', 'right_answer_stylish.txt', 'right_answer_plain.txt', 'right_answer_json.json')
    ]
)
def test_diff_stylish_json(file1, file2, right_answer_stylish, right_answer_plain, right_answer_json):
    path_dict1 = get_fixture_path(file1)
    path_dict2 = get_fixture_path(file2)

    assert generate_diff(path_dict1, path_dict2) == right_answer_stylish
    assert generate_diff(path_dict1, path_dict2, 'plain') == right_answer_plain
    assert generate_diff(path_dict1, path_dict2, 'json') == right_answer_json


def get_fixture_path(file_name):
    return Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)
