import json
import yaml

from gendiff.constants import DATA_FORMAT_CHOICES


def parse_data(data, data_format):
    if data_format == DATA_FORMAT_CHOICES.JSON:
        return json.loads(data)
    elif data_format == DATA_FORMAT_CHOICES.YAML:
        return yaml.safe_load(data)
    else:
        raise ValueError(
            f'Unsupported format: {data_format}'
        )
