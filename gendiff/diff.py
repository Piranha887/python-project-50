def create_diff(data1, data2):
    """Create a list of differences between two dictionaries."""
    result = []
    if data1 is None:
        data1 = {}
    if data2 is None:
        data2 = {}
    keys = set(data1.keys()).union(data2.keys())
    for key in sorted(keys):
        if key not in data1:
            result.append({'status': 'added', 'name': key, 'data': data2[key]})
        elif key not in data2:
            result.append({'status': 'deleted', 'name': key, 'data': data1[key]})
        elif data1[key] == data2[key]:
            result.append({'status': 'not changed', 'name': key, 'data': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({'status': 'nested', 'name': key, 'children': create_diff(data1[key], data2[key])})
        else:
            result.append({'status': 'changed', 'name': key, 'data before': data1[key], 'data after': data2[key]})
    return result
