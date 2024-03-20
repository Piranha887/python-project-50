"""Json format formater."""

import json


def format_json(diff_list):
    return json.dumps(diff_list, indent=4)
