"""Json format formater."""

import json

import copy


def format_json(diff_list):
    return json.dumps(diff_list, indent=2)
