"""Test generate_diff"""

import pytest
from gendiff.generate_diff import generate_diff
from gendiff.constants import STYLE_FORMATS
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent.absolute() / 'fixtures'

FILES = [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
]

RIGHT_ANSWERS = {
    STYLE_FORMATS.STYLISH: 'right_answer_stylish.txt',
    STYLE_FORMATS.PLAIN: 'right_answer_plain.txt',
    STYLE_FORMATS.JSON: 'right_answer_json.json'
}


@pytest.mark.parametrize(
    "file1,file2",
    FILES
)
def test_diff_stylish_json(file1, file2):
    path_dict1 = FIXTURES_DIR / file1
    path_dict2 = FIXTURES_DIR / file2

    for format, right_answer in RIGHT_ANSWERS.items():
        assert generate_diff(path_dict1, path_dict2, format) == (FIXTURES_DIR / right_answer).read_text()


def get_fixture_path(file_name):
    return FIXTURES_DIR / file_name
