import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        # TODO: add assertions for subtract
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(2, -2), 4)

    def test_multiply(self):
        # TODO: add assertions for multiply
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(1, -2), -2)
        self.assertEqual(multiply(-2, -2), 4)


    def test_divide(self):
        # TODO: add assertions for divide
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(2, 0), "cannot divide by zero")
        self.assertEqual(divide(1, 2), 0.5)

if __name__ == '__main__':
    unittest.main()
