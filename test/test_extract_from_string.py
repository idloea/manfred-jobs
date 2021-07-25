import unittest

from extract_from_string import extract_number_list_from_spaced_string, extract_currency_from_spaced_string, \
    extract_percentage_number_from_spaced_string


class test_digit_from_string(unittest.TestCase):
    def test_extract_number_list_from_spaced_string(self):
        example_string = 'Salary 100-110.5k€ + 10% variable per year and 50% remote work'
        result = extract_number_list_from_spaced_string(example_string)
        expected_result = [100, 110.5, 10, 50]
        self.assertEqual(expected_result, result)


class test_currency_from_string(unittest.TestCase):
    def test_extract_currency_from_spaced_string(self):
        example_string = 'Salary between 100k€-110k€'
        result = extract_currency_from_spaced_string(example_string)
        expected_result = '€'
        self.assertEqual(expected_result, result)


class test_percentage_from_string(unittest.TestCase):
    def test_extract_percentage_number_from_spaced_string(self):
        example_string = 'Salary between 80k€-90k€ and 100% remote'
        result = extract_percentage_number_from_spaced_string(example_string)
        expected_result = ['100%']
        self.assertEqual(expected_result, result)


class test_percentage_from_string(unittest.TestCase):
    def test_extract_percentage_number_from_spaced_string(self):
        example_string = 'Salary between 80k€-90k€ and 100% remote plus 10.25% variable'
        result = extract_percentage_number_from_spaced_string(example_string)
        expected_result = [100, 10.25]
        self.assertEqual(expected_result, result)
