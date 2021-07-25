import re


def extract_number_list_from_spaced_string(spaced_string: str) -> list:
    pattern = r'\d+(?:\.\d+)?'
    return [float(string) for string in re.findall(pattern, spaced_string)]


def extract_currency_from_spaced_string(spaced_string: str) -> str:
    pattern = r'[$€£]'
    currency_list = [string for string in re.findall(pattern, spaced_string)]
    if not currency_list:
        return '€'
    else:
        return currency_list[0]
