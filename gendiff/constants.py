from collections import namedtuple

_STYLE_FORMAT_VALUES = ('stylish', 'plain', 'json')
STYLE_FORMATS = namedtuple('FormatChoices',
                           map(str.upper, _STYLE_FORMAT_VALUES))(*_STYLE_FORMAT_VALUES)

_DIFF_CHANGES_TYPE_VALUES = ('deleted', 'added', 'nested', 'changed', 'unchanged')
DIFF_CHANGES_TYPES = namedtuple('FormatTypes',
                                map(str.upper, _DIFF_CHANGES_TYPE_VALUES))(*_DIFF_CHANGES_TYPE_VALUES)

_DATA_FORMATS_VALUE = ('json', 'yaml')
DATA_FORMATS = namedtuple('DataFormats',
                          map(str.upper, _DATA_FORMATS_VALUE))(*_DATA_FORMATS_VALUE)
