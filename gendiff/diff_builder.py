def create_diff(data1, data2):
    """Create a list of differences between two dictionaries."""
    result = {}
    if data1 is None:
        data1 = {}
    if data2 is None:
        data2 = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key not in data2:
            result[key] = {'status': 'deleted', 'name': key, 'data': data1[key]}
        elif data1[key] != data2[key]:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[key] = {'status': 'nested', 'name': key, 'children': create_diff(data1[key], data2[key])}
            else:
                result[key] = {'status': 'changed', 'name': key, 'data before': data1[key], 'data after': data2[key]}
        elif key not in data1:
            result[key] = {'status': 'added', 'name': key, 'data': data2[key]}
    return result

