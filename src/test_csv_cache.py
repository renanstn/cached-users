import unittest
import os
import csv
import src.csv_cache as cache


class TestCsvCache(unittest.TestCase):

    cache = cache.CsvCache()
    user_data = {
        'username': 'user_test',
        'email': 'test@test.com',
        'website': 'www.test.com',
        'hemisphere': 'sul'
    }

    def tearDown(self):
        path = os.path.abspath(os.getcwd())
        if os.path.exists(path + '/cache.csv'):
            os.remove(path + '/cache.csv')

    def test_save_cache(self):
        self.cache.save_cache(self.user_data)
        self.assertTrue(os.path.exists('cache.csv'))
        with open('cache.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for user_cached in reader:
                if user_cached['username'] == self.user_data['username']:
                    self.assertEqual(user_cached['email'], 'test@test.com')
                    self.assertEqual(user_cached['website'], 'www.test.com')
                    self.assertEqual(user_cached['hemisphere'], 'sul')

    def test_check_cache(self):
        self.cache.save_cache(self.user_data)

        user = self.cache.check_cache('user_test')
        self.assertEqual(user['username'], self.user_data['username'])
        self.assertEqual(user['email'], self.user_data['email'])
        self.assertEqual(user['website'], self.user_data['website'])
        self.assertEqual(user['hemisphere'], self.user_data['hemisphere'])
