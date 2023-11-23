import unittest
import datetime

import requests

from join_words import join_words
from unittest.mock import Mock, MagicMock, patch


def my_print(text, visible=True):
    if visible:
        print(text)


def mocked_get(*args, **kwargs):
    return join_words('badger', 'racoon')


def mocked_get_1(*args, **kwargs):
    return f'404'


class TestJoinWords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        my_print('A test beings')

    @classmethod
    def tearDownClass(cls):
        my_print('A test ends')

    def setUp(self):
        my_print('A test suite begins')

    def tearDown(self):
        my_print('A test suite ends')

    def test_join_words(self):
        result = join_words('Мамин', 'Сибиряк')
        self.assertEqual(result, 'Мамин-Сибиряк')

    @unittest.skip('Это его настоящая фамилия')
    def test_skip_test(self):
        result = join_words('Мамин', 'Сибиряк')
        self.assertEqual(result, 'Мамин')

    @unittest.expectedFailure
    def test_xfail(self):
        result = join_words('Салтыков', 'Щедрин')
        self.assertEqual(result, 'Солженицын')

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        response = requests.get("https://www.google.com/search?q=badger")
        self.assertEqual(response, "badger-racoon")

    @unittest.skipIf(
        datetime.datetime.now().weekday() == 0 or datetime.datetime.now().weekday() == 2 or
        datetime.datetime.now().weekday() == 4,
        'Потому что сегодня понедельник, среда или пятница')
    def test_skip_if_test(self):
        raise Exception('!!!')

    @patch("requests.get", side_effect=mocked_get_1)
    def test_mock_1(self, mock):
        response = requests.get('https://www.google.com')
        self.assertEqual(response, '404')





