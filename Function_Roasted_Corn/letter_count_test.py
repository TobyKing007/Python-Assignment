from unittest import TestCase

from letter_count import letter_count

class TestClass (TestCase):

    def test_empty_string(self):
        valid_check = (letter_count("") == 0)
        self.assertTrue(valid_check)

    def test_single_character(self):
        valid_check = (letter_count("a") == 1)
        self.assertTrue(valid_check)

    def test_multiple_characters(self):
         valid_check = (letter_count("story") == 5)
         self.assertTrue(valid_check)

    def test_string_with_spaces(self):
        valid_check = (letter_count("agricultural science") == 20)
        self.assertTrue(valid_check)

    def test_string_with_numbers(self):
        valid_check = (letter_count("12345") == 5)
        self.assertTrue(valid_check)

    def test_string_with_special_characters(self):
        valid_check = (letter_count("!@#$%") == 5)
        self.assertTrue(valid_check)

    def test_string_with_mixed_characters(self):
        valid_check = (letter_count("Hi! 123") == 7)
        self.assertTrue(valid_check)

    def test_incorrect_length_false(self):
        valid_check = (letter_count("sacrifice") == 10)
        self.assertFalse(valid_check)


