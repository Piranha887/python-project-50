def create_difference_tree(old_data, new_data, diff={}):
    merged_keys = old_data.keys() | new_data.keys()
    for key in sorted(merged_keys):
        if key not in new_data:
            diff[key] = {'value': old_data[key],
                         'status': 'removed'}
        elif key not in old_data:
            diff[key] = {'value': new_data[key],
                         'status': 'added'}
        elif new_data[key] == old_data[key]:
            diff[key] = {'value': new_data[key],
                         'status': 'unchanged'}
        elif type(old_data[key]) is dict and type(new_data[key]) is dict:
            diff[key] = {}
            create_difference_tree(old_data[key], new_data[key], diff[key])
        else:
            diff[key] = {'value': {'old': old_data[key],
                                   'new': new_data[key]},
                         'status': 'changed'}
    return diff
