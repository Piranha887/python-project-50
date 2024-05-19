from gendiff.formatters.json import format_json
from gendiff.formatters.plain import convert_to_plain_text
from gendiff.formatters.stylish import render_stylish
from gendiff.constants import STYLE_FORMAT_CHOICES


def format_diff(diff, formatter):
    match formatter:
        case STYLE_FORMAT_CHOICES.STYLISH:
            return render_stylish(diff)
        case STYLE_FORMAT_CHOICES.PLAIN:
            return convert_to_plain_text(diff)
        case STYLE_FORMAT_CHOICES.JSON:
            return format_json(diff)

    raise Exception("Inexistent output formatter, please use 'plain', "
                    "'stylish' or none which equals to 'stylish'")
