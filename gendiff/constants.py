from collections import namedtuple

_STYLE_FORMAT_VALUES = ('stylish', 'plain', 'json')
STYLE_FORMAT_CHOICES = (namedtuple('StyleFormatChoices',
                                   map(str.upper, _STYLE_FORMAT_VALUES))(*_STYLE_FORMAT_VALUES))  # noqa

_DIFF_CHANGE_TYPES_VALUES = \
    ('deleted', 'added', 'nested', 'modified', 'unchanged')
DIFF_CHANGE_TYPES = (namedtuple('DiffChangeTypes',
                                map(str.upper, _DIFF_CHANGE_TYPES_VALUES))(*_DIFF_CHANGE_TYPES_VALUES))  # noqa

_DATA_FORMAT_VALUES = ('json', 'yaml', 'yml')
DATA_FORMAT_CHOICES = (namedtuple('DataFormatChoices',
                                  map(str.upper, _DATA_FORMAT_VALUES))(*_DATA_FORMAT_VALUES))  # noqa

INDENT = '    '
