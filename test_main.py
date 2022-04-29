from main import get_message
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        f = get_message("http://localhost")
        self.assertEqual(f["Url"], "http://localhost")