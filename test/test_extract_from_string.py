import unittest

from extract_from_string import extract_number_list_from_spaced_string


class test_digit_from_string(unittest.TestCase):
    def test_extract_number_list_from_string(self):
        example_string = 'Salary 100-110.5k€ + 10% variable per year and 50% remote work'
        result = extract_number_list_from_spaced_string(example_string)
        expected_result = [100, 110.5, 10, 50]
        self.assertEqual(expected_result, result)
