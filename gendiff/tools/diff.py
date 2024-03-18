def diff(dict1, dict2):
    """Create a list of differences between two dictionaries."""
    result = []
    keys = set(dict1.keys()).union(dict2.keys())
    for key in sorted(keys):
        if key not in dict1:
            result.append({'status': 'added', 'name': key, 'data': dict2[key]})
        elif key not in dict2:
            result.append({'status': 'deleted', 'name': key, 'data': dict1[key]})
        elif dict1[key] == dict2[key]:
            result.append({'status': 'not changed', 'name': key, 'data': dict1[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result.append({'status': 'nested', 'name': key, 'children': diff(dict1[key], dict2[key])})
        else:
            result.append({'status': 'changed', 'name': key, 'data before': dict1[key], 'data after': dict2[key]})
    return result