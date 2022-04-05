import unittest
import testAPI
from datetime import datetime, timedelta
import pytz


class TestStringMethods(unittest.TestCase):


    def test_request_status(self):
        """testing the service is up"""
        data_expected = 200
        test1 = testAPI.TestAPI()
        response = test1._get_status()
        self.assertEqual(response, data_expected)


    def test_request_time(self):
        """testing the articles loaded were published within the last week"""
        tz = pytz.timezone('Europe/London')
        today = datetime.now(tz)
        last_week = today - timedelta(days = 7)
        test2 = testAPI.TestAPI()
        response_date = test2.test_get()
        self.assertTrue(today > response_date)
        self.assertTrue(last_week < response_date)


if __name__ == '__main__':
    unittest.main()