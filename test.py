import unittest
from main import add, subtract, multiply, divide
from main import check
from main import remainder

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5), 7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)


class TestDivide(unittest.TestCase):
   def test_divide_success(self):
       self.assertEqual(divide(10, 2), 5)
       self.assertEqual(divide(6, 3), 2)
       self.assertEqual(divide(70, 2), 35)

   def test_divide_by_zero(self):
       self.assertRaises(ValueError, divide, 6, 0)


class TestCheck(unittest.TestCase):
   def test_check(self):
       self.assertTrue(check(2))
       self.assertTrue(check(6))
       self.assertTrue(check(220))
       self.assertFalse(check(1))
       self.assertFalse(check(3))
       self.assertFalse(check(57))


class TestRemainderFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), -1)
        self.assertEqual(remainder(10, -3), 1)
        self.assertEqual(remainder(-10, -3), -1)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 3), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)


if __name__ == '__main__':
   unittest.main()
