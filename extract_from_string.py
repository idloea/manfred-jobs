import re


def extract_number_list_from_spaced_string(spaced_string: str) -> list:
    pattern = r'\d+(?:\.\d+)?'
    return [float(string) for string in re.findall(pattern, spaced_string)]

