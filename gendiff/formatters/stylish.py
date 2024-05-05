import json

SYMBOLS = {
    'added': '  + ',
    'removed': '  - ',
    'untouched': '    '
}


def stringify(diff, level=1):
    result = '{\n'
    indent = "    "

    if isinstance(diff, str):
        return diff

    if isinstance(diff, bool):
        return 'true' if diff else 'false'

    if isinstance(diff, dict):
        for key, value in diff.items():
            result += f'{indent * level}{key}: '
            result += f'{stringify(value, level + 1)}\n'
        result += f'{indent * (level - 1)}}}'

        return result

    else:
        return json.dumps(diff)


def render_stylish(object_dict, level=0):
    result = '{\n'
    level += 1

    for key, value in object_dict.items():
        indent = SYMBOLS['untouched'] * (level - 1)
        types = value.get('type')
        values = value.get('value')
        children = value.get('children')

        if types == 'added' or types == 'removed' \
                or types == 'untouched':
            result += f'{indent}{SYMBOLS[types]}{key}: '
            result += f'{stringify(values, level + 1)}\n'

        elif types == 'changed':
            result += f'{indent}{SYMBOLS["removed"]}{key}: '
            result += f'{stringify(values.get("old_value"), level + 1)}\n'
            result += f'{indent}{SYMBOLS["added"]}{key}: '
            result += f'{stringify(values.get("new_value"), level + 1)}\n'

        elif types == 'dictionary':
            result += f'{indent}{SYMBOLS["untouched"]}{key}: '
            result += f'{render_stylish(children, level)}\n'
    result += f'{indent}}}'
    return result
