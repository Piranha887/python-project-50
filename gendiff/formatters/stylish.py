def stylish(diff_list):
    """Converts a list of differences to dictionary format. Returns string."""
    return get_diff_stylish(diff_list)


def get_diff_stylish(diff_list, level=0):
    result = ['{']
    indent = '  '
    for i in range(level):
        indent += '    '
    # Отсортируем ключи в словарях перед сравнением
    for node in diff_list:
        if node['status'] == 'nested':
            data = get_diff_stylish(node['children'], level + 1)
            result.append(f"{indent}  {node['name']}: {data}")
        if node['status'] == 'not changed':
            data = format_data(node['data'], indent)
            result.append(f"{indent}  {node['name']}: {data}")
        if node['status'] == 'added':
            data = format_data(node['data'], indent)
            result.append(f"{indent}+ {node['name']}: {data}")
        if node['status'] == 'deleted':
            data = format_data(node['data'], indent)
            result.append(f"{indent}- {node['name']}: {data}")
        if node['status'] == 'changed':
            if 'data before' in node:
                data_before = format_data(node['data before'], indent)
                result.append(f"{indent}- {node['name']}: {data_before}")
            if 'data after' in node:
                data_after = format_data(node['data after'], indent)
                result.append(f"{indent}+ {node['name']}: {data_after}")
    result.append(indent[:-2] + '}')
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
