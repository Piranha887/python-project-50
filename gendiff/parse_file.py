import json
import yaml

from gendiff.constants import DATA_FORMATS


def parse_data(data, data_format):
    match data_format:
        case DATA_FORMATS.JSON:
            return json.load(data)
        case DATA_FORMATS.YAML:
            return yaml.safe_load(data)

    ValueError(f'Unsupported extension: {data_format}. Supported [{", ".join(DATA_FORMATS)}]')
