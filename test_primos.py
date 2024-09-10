import unittest
from primos import is_prime

class TestPrimos(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
    
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

if __name__ == '__main__':
    unittest.main()
