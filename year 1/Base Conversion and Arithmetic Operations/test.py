# name: MARTA RARES-PETRU
# group: 1012
# specialisation: AI
# teacher: LUPEA MIHAELA

# This file contains test functions and data examples

import unittest
from main import *
from utils import *


class TestFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition("10", "01", 2), "11")
        self.assertEqual(addition("FF", "1", 16), "100")
        self.assertEqual(addition("1010", "1101", 2), "10111")

    def test_subtraction(self):
        self.assertEqual(subtraction("10", "01", 2), "1")
        self.assertEqual(subtraction("FF", "1", 16), "FE")
        self.assertEqual(subtraction("1101", "1010", 2), "11")

    def test_multiplication(self):
        self.assertEqual(multiplication("10", "2", 10), "20")
        self.assertEqual(multiplication("ABC", "2", 16), "1578")
        self.assertEqual(multiplication("101", "11", 2), "1111")

    def test_division(self):
        self.assertEqual(division("10", "2", 10), ("5", "0"))
        self.assertEqual(division("ABC", "2", 16), ("55E", "0"))
        self.assertEqual(division("1111", "11", 2), ("101", "0"))

    def test_base_p_to_base_2(self):
        self.assertEqual(base_p_to_base_2("231", 4), "101101")
        self.assertEqual(base_p_to_base_2("1A", 16), "00011010")
        self.assertEqual(base_p_to_base_2("12", 8), "001010")

    def test_base_2_to_base_q(self):
        self.assertEqual(base_2_to_base_q("101010", 4), "222")
        self.assertEqual(base_2_to_base_q("11010", 8), "32")
        self.assertEqual(base_2_to_base_q("1111", 16), "F")

    def test_intermediate_base(self):
        self.assertEqual(intermediate_base("10", 2, 10), "2")
        self.assertEqual(intermediate_base("1A", 16, 2), "11010")
        self.assertEqual(intermediate_base("101", 2, 16), "5")

    def test_substitution_method(self):
        self.assertEqual(substitution_method("10", 2, 16), "2")
        self.assertEqual(substitution_method("1A", 16, 2), "11010")
        self.assertEqual(substitution_method("101", 2, 10), "5")

    def test_successive_div_and_mult(self):
        self.assertEqual(successive_div_and_mult("2", 16, 2), "10")
        self.assertEqual(successive_div_and_mult("1A", 16, 2), "11010")
        self.assertEqual(successive_div_and_mult("101", 5, 3), "222")

    def test_to_base_2(self):
        self.assertEqual(to_base_2('A'), '1010')
        self.assertEqual(to_base_2('5'), '101')
        self.assertEqual(to_base_2('F'), '1111')

    def test_base_power(self):
        self.assertEqual(base_power(16), 4)
        self.assertEqual(base_power(4), 2)
        self.assertEqual(base_power(8), 3)

    def test_convert(self):
        self.assertEqual(convert("1010", 2, 10), "10")
        self.assertEqual(convert("AB", 16, 10), "171")
        self.assertEqual(convert("1001", 2, 16), "9")

    def test_power(self):
        self.assertEqual(power("10", 3, 10), "1000")
        self.assertEqual(power("A", 2, 16), "64")

    def test_simplify(self):
        self.assertEqual(simplify("00012"), "12")
        self.assertEqual(simplify("123000"), "123000")
        self.assertEqual(simplify("000.000"), "0")


if __name__ == '__main__':
    unittest.main()