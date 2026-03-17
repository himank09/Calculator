import unittest
from calculator import add, subtract, multiply, divide, power, square_root, modulus

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-2, 2), 4)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(-4), "Error: Cannot square root a negative number")

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 0), "Error: Cannot divide by zero")
        self.assertEqual(modulus(9, 3), 0)

if __name__ == "__main__":
    unittest.main()