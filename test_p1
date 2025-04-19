import unittest
from p1 import arithmetic 

class ArithmeticTestCase(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(arithmetic(3, 4, '+'), 7)

    def test_minus(self):
        self.assertEqual(arithmetic(3, 4, '-'), -1)

    def test_multiply(self):
        self.assertEqual(arithmetic(3, 4, '*'), 12)

    def test_divide(self):
        self.assertAlmostEqual(arithmetic(3, 4, '/'), 0.75)

    def test_unknown(self):
        self.assertEqual(arithmetic(3, 4, '.'), "Неизвестная операция")

if __name__ == "__main__":
    unittest.main()
