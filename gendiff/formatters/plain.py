'''Flat format formater.'''


def plain(diff_list):
    """Converts a list of differences to flat format. Returns string."""
    diff_list.sort(key=lambda x: x['name'])
    result = get_diff_plain_list(diff_list)
    return '\n'.join(result)


def get_diff_plain_list(diff_list, path=''):
    """Analysis of the nodes. Returns a list with changes."""
    result = []
    for node in diff_list:
        if node['status'] == 'nested':
            path_to_change = path + node['name'] + '.'
            difference = get_diff_plain_list(node['children'], path_to_change)
            result.extend(difference)
        if node['status'] == 'added':
            path_to_change = path + node['name']
            change = to_str(node['data'])
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['status'] == 'deleted':
            path_to_change = path + node['name']
            change = to_str(node['data'])
            difference = "Property '{}' was removed".format(path_to_change)
            result.append(difference)
        if node['status'] == 'changed':
            path_to_change = path + node['name']
            change_before = to_str(node['data before'])
            change_after = to_str(node['data after'])
            difference = (
                f"Property '{path_to_change}' was updated. "
                f"From {change_before} to {change_after}"
            )
            result.append(difference)
    return result


def to_str(value):
    """Parses the node data. Returns it in the correct format as a string."""
    if isinstance(value, (dict, list)):
        result = '[complex value]'
    elif isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    elif isinstance(value, str):
        result = f"'{value}'"
    else:
        result = str(value)
    return result
