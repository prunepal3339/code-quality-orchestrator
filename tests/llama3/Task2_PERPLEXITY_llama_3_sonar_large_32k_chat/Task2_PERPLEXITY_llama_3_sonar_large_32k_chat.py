import pytest
from output.llama3.Task2_PERPLEXITY_llama_3_sonar_large_32k_chat import create_phone_number
import unittest


class TestCreatePhoneNumber(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

    def test_all_zeros(self):
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

    def test_all_nines(self):
        self.assertEqual(create_phone_number([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]), "(999) 999-9999")

    def test_alternating_digits(self):
        self.assertEqual(create_phone_number([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]), "(101) 010-1010")

    def test_ascending_order(self):
        self.assertEqual(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), "(012) 345-6789")

    def test_descending_order(self):
        self.assertEqual(create_phone_number([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), "(987) 654-3210")

    def test_repeated_digits(self):
        self.assertEqual(create_phone_number([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]), "(111) 222-3333")

    def test_random_mix(self):
        self.assertEqual(create_phone_number([5, 2, 9, 3, 7, 1, 0, 8, 6, 4]), "(529) 371-0864")

    def test_another_random_mix(self):
        self.assertEqual(create_phone_number([7, 4, 2, 8, 5, 0, 9, 1, 3, 6]), "(742) 850-9136")

    def test_edge_case(self):
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 2]), "Invalid phone number")

if __name__ == '__main__':
    unittest.main()
