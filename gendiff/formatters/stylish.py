def stylish(diff_list):
    """Converts a list of differences to dictionary format. Returns string."""
    return get_diff_stylish(diff_list)


def get_diff_stylish(diff_list, level=0):
    """Converts a list of differences to dictionary format. Returns string."""
    result = ['{']
    for node in diff_list:
        if node['status'] == 'nested':
            data = stylish(node['children'])
            result.append(f"  {node['name']}: {data}")
        elif node['status'] == 'not changed':
            data = format_data(node['data'])
            result.append(f"    {node['name']}: {data}")
        elif node['status'] == 'added':
            data = format_data(node['data'])
            result.append(f"  + {node['name']}: {data}")
        elif node['status'] == 'deleted':
            data = format_data(node['data'])
            result.append(f"  - {node['name']}: {data}")
        elif node['status'] == 'changed':
            data_before = format_data(node['data before'])
            data_after = format_data(node['data after'])
            result.append(f"  - {node['name']}: {data_before}")
            result.append(f"  + {node['name']}: {data_after}")
    result.append('}')
    return '\n'.join(result)


def format_data(data, indent):
    result = []
    if isinstance(data, dict):
        result.append('{')
        for key, value in sorted(data.items()):
            result.append(f'{indent}  {key}: {format_data(value, indent + "    ")}')
        result.append(f'{indent}}}')
    elif isinstance(data, list):
        result.append('[')
        for item in data:
            result.append(f'{indent}  {format_data(item, indent + "    ")}')
        result.append(f'{indent}]')
    elif data is None:
        result.append('null')
    elif isinstance(data, bool):
        result.append('true' if data else 'false')
    else:
        result.append(str(data))
    return '\n'.join(result)
