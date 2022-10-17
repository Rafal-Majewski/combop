import unittest

from ...python_project_template.mymathpackage import is_even


class IsEvenTest(unittest.TestCase):
    def test_is_2_even(self):
        self.assertTrue(is_even(2))

    def test_is_3_even(self):
        self.assertFalse(is_even(3))

    def test_is_empty_string_even(self):
        self.assertFalse(is_even(""))
