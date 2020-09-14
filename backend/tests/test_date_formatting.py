import unittest
from utils.date_formatter import DateFormatter

class DateFormatTestCase(unittest.TestCase):
    def setUp(self):
        self.test_valid_date_details = {'January 20, 2019': '%B %d, %Y'}
        self.test_invalid_date_details = {'February 30, 2014': '%B %d, %Y'}
        self.expected_date_value = '2019-01-20'

    def test_generating_date_from_valid_date_value(self):
        test_date_format = DateFormatter(list(self.test_valid_date_details)[0], list(self.test_valid_date_details.values())[0])
        actual_date_value = test_date_format._date()
        self.assertEqual(actual_date_value, self.expected_date_value)

    def test_generating_date_from_invalid_date_value(self):
        test_date_format = DateFormatter(list(self.test_invalid_date_details)[0], list(self.test_valid_date_details.values())[0])
        invalid_date_value = test_date_format._date()
        self.assertEqual(invalid_date_value, "Error")

if __name__ == "__main__":
    unittest.main()