from functions import *
import unittest


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        # test prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(17))

        # test non prime numbers
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

        # test edge cases 0 and 1
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

        # test negative numbers are not prime
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-10))

class TestRemoveVowels(unittest.TestCase):
    def test_remove_vowels(self):
        # test only lowercase vowels included
        self.assertEqual(remove_vowels("hello"), "hll")
        self.assertEqual(remove_vowels("aeiou"), "")
        self.assertEqual(remove_vowels("programming"), "prgrmmng")

        # test only uppercase vowels included
        self.assertEqual(remove_vowels("HELLO"), "HLL")
        self.assertEqual(remove_vowels("AEIOU"), "")
        self.assertEqual(remove_vowels("PYTHON"), "PYTHN")

        # test mix of upper and lower case vowels
        self.assertEqual(remove_vowels("HeLLo WoRLd"), "HLL WRLd")
        self.assertEqual(remove_vowels("AeIoU"), "")

        # test no vowels
        self.assertEqual(remove_vowels("xyz"), "xyz")
        self.assertEqual(remove_vowels("bcdfg"), "bcdfg")

        # test only vowels
        self.assertEqual(remove_vowels("aaa"), "")
        self.assertEqual(remove_vowels("EEE"), "")

        # test empty string
        self.assertEqual(remove_vowels(""), "")

        # test Y
        self.assertEqual(remove_vowels("yellow"), "yllw")
        self.assertEqual(remove_vowels("SYMPHONY"), "SYMPHNY")
        self.assertEqual(remove_vowels("yay"), "yy")

if __name__ == "__main__":
    unittest.main()