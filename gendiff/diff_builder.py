from gendiff.constants import DIFF_CHANGE_TYPES


def create_difference_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = {}
    for key in keys:
        if key not in data2:
            result[key] = {
                'type': DIFF_CHANGE_TYPES.DELETED,
                'value': data1[key]
            }
        elif key not in data1:
            result[key] = {
                'type': DIFF_CHANGE_TYPES.ADDED,
                'value': data2[key]
            }

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'type': DIFF_CHANGE_TYPES.NESTED,
                'children': create_difference_tree(data1[key], data2[key]),
            }

        elif isinstance(data1[key], list) and isinstance(data2[key], list):
            children = []
            for i in range(max(len(data1[key]), len(data2[key]))):
                if i >= len(data1[key]):
                    children.append({
                        'type': DIFF_CHANGE_TYPES.ADDED,
                        'value': data2[key][i]
                    })
                elif i >= len(data2[key]):
                    children.append({
                        'type': DIFF_CHANGE_TYPES.DELETED,
                        'value': data1[key][i]
                    })
                elif data1[key][i] != data2[key][i]:
                    children.append({
                        'type': DIFF_CHANGE_TYPES.MODIFIED,
                        'old_value': data1[key][i],
                        'new_value': data2[key][i]
                    })
                else:
                    children.append({
                        'type': DIFF_CHANGE_TYPES.UNCHANGED,
                        'value': data1[key][i]
                    })
            result[key] = {
                'type': DIFF_CHANGE_TYPES.NESTED,
                'children': children
            }

        elif data1[key] != data2[key]:
            result[key] = {
                'type': DIFF_CHANGE_TYPES.MODIFIED,
                'old_value': data1[key],
                'new_value': data2[key]
            }
        else:
            result[key] = {
                'type': DIFF_CHANGE_TYPES.UNCHANGED,
                'value': data1[key]
            }

    return result
