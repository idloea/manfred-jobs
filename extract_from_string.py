import re


def extract_number_list_from_spaced_string(spaced_string: str) -> list:
    pattern = r'\d+(?:\.\d+)?'
    return [float(string) for string in re.findall(pattern, spaced_string)]


def extract_currency_from_spaced_string(spaced_string: str) -> str:
    pattern = r'[$€£]'
    currency_list = [string for string in re.findall(pattern, spaced_string)]
    if not currency_list:
        return '€'  # As Manfred is located in Spain, the assumption is to consider offers without currency in €
    else:
        return currency_list[0]


def extract_percentage_number_from_spaced_string(spaced_string: str) -> list:
    pattern = r'(\d+|\d+[.,]\d{1,2})(?=\s*%)'
    return [float(string) for string in re.findall(pattern, spaced_string)]
