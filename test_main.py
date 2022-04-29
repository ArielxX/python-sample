from main import get_message
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        f = get_message("hhtp://localhost")
        self.assertEqual(f.Url == "hhtp://localhost")