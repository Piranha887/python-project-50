import pytest
from gendiff import generate_diff
import difflib

JSON_FLAT_OLD = 'tests/fixtures/file1.json'
JSON_FLAT_NEW = 'tests/fixtures/file2.json'
YML_FLAT_OLD = 'tests/fixtures/file1.yml'
YML_FLAT_NEW = 'tests/fixtures/file2.yml'
STYLISH_FLAT_RESULT = 'tests/fixtures/right_answer_stylish.txt'
PLAIN_FLAT_RESULT = 'tests/fixtures/right_answer_plain.txt'
JSON_FLAT_RESULT = 'tests/fixtures/right_answer_json.json'


@pytest.fixture
def get_result():
    def _get_result(format):
        with open(format, 'r') as result:
            expected = result.read()
        return expected

    return _get_result


def normalize_output(output):
    return '\n'.join(line.rstrip()
                     for line in output.splitlines() if line.strip())


def test_exception():
    with pytest.raises(Exception) as exc_info:
        generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'wrong_formatter')
    assert str(exc_info.value) == \
           "Inexistent output formatter, please use 'plain', " \
           "'stylish' or none which equals to 'stylish'"


def test_generate_diff_plain(get_result):
    assert generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'plain') ==\
           get_result(PLAIN_FLAT_RESULT)
    assert generate_diff(YML_FLAT_OLD, YML_FLAT_NEW, 'plain') ==\
           get_result(PLAIN_FLAT_RESULT)


def test_generate_diff_stylish(get_result):
    result = generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'stylish')
    expected = get_result(STYLISH_FLAT_RESULT)

    if normalize_output(result) != normalize_output(expected):
        print("Differences:")
        for line in difflib.unified_diff(result.splitlines(),
                                         expected.splitlines(),
                                         fromfile='result',
                                         tofile='expected'):
            print(line)

    assert normalize_output(result) == normalize_output(expected)


def test_generate_diff_json(get_result):
    result = generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'json')
    expected = get_result(JSON_FLAT_RESULT)

    if normalize_output(result) != normalize_output(expected):
        print("Differences:")
        for line in difflib.unified_diff(result.splitlines(),
                                         expected.splitlines(),
                                         fromfile='result',
                                         tofile='expected'):
            print(line)

    assert normalize_output(result) == normalize_output(expected)
