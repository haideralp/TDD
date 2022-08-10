from calc import BasicCalc
import unittest
import pytest

class Calc_tests(unittest.TestCase):
    calc_obj = BasicCalc()
    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(8, 5), 3)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(10, 5), 2)

    def test_dob(self):
        self.assertEqual(self.calc_obj.dob(7,12),7,12)

    def test_percentage(self):
        self.assertEqual((self.calc_obj.percentage(7,8),87.5)