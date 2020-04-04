"""
    Implementation of a Test suite for HW_02 Fraction Calculator for addtion, subtraction, multiplication, division,
    equality, not equal, less than, less than or equal, greater than, greater than or equal 
"""

import unittest
from HW03_Dhruv_Patel import Fraction
 

class TestFraction(unittest.TestCase):
    """ test class Fraction """
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f34: Fraction = Fraction(3, 4)
        f1: Fraction = Fraction(1, 1)

        self.assertEqual(f34.numerator, 3)
        self.assertEqual(f34.denominator, 4)
        self.assertNotEqual(f34.numerator, f1.numerator)

    def test_init_exception(self):
        """ verify that ZeroDivisionError is raised when appropriate """
        with self.assertRaises(ZeroDivisionError):
            Fraction(2, 0)
    
    def test_str(self):
        """verify string"""
        f12: Fraction = Fraction(1, 2)

        self.assertEqual(str(f12), '1 / 2')
        # self.assertNotEqual(str(f12), '1/2')

    def test_add(self):
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)

        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_3_operands(self):
        """ verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)

        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))

    def test_sub(self):
        """verify fraction subtraction"""
        f34: Fraction = Fraction(3, 4)
        f12: Fraction = Fraction(1, 2)

        self.assertEqual(f34 - f12, Fraction(2, 8))
        self.assertEqual(f34, Fraction(3, 4))
    
    def test_mul(self):
        """verify fraction multiplication"""
        f128: Fraction = Fraction(12, 8)
        f69: Fraction = Fraction(6, 9)
        f01: Fraction = Fraction(0, 1)

        self.assertEqual(f128 * f69, Fraction(72, 72))
        self.assertTrue(f01 * f69 == Fraction(0, 9))

    def test_truediv(self):
        """verify fraction division"""
        f128: Fraction = Fraction(12, 8)
        f69: Fraction = Fraction(6, 9)

        self.assertEqual(f128 / f69, Fraction(108, 48))
    
    def test_eq(self):
        """verify fraction equality"""
        f24: Fraction = Fraction(2, 4)
        f36: Fraction = Fraction(3, 6)
        f34: Fraction = Fraction(3, 4)

        self.assertEqual(f24, f36)
        self.assertNotEqual(f24, f34)
    
    def test_ne(self):
        """verify not equal fraction"""
        f13: Fraction = Fraction(1, 3)
        f45: Fraction = Fraction(4, 5)
        f26: Fraction = Fraction(2, 6)

        self.assertNotEqual(f13, f45)
        self.assertEqual(f13, f26)
        self.assertTrue(f26 != f45)
    
    def test_lt(self):
        """verify less than fraction"""
        f13: Fraction = Fraction(1, 3)
        f45: Fraction = Fraction(4, 5)
        f58: Fraction = Fraction(5, 8)
        
        f1: Fraction = Fraction(-1, 3)
        f2: Fraction = Fraction(1, -3)
        f23: Fraction = Fraction(2, 3)
        
        self.assertLess(f13, f45)
        self.assertFalse(f45 < f58)
        self.assertTrue(f1 < f23)
        self.assertTrue(f2 < f23)
    
    def test_le(self):
        """verify less than or equal fraction"""
        f810: Fraction = Fraction(8, 10)
        f45: Fraction = Fraction(4, 5)
        f73: Fraction = Fraction(7, 3)

        self.assertLessEqual(f45, f810)
        self.assertTrue(f73 <= f73)
        self.assertFalse(f73 <= f810)
    
    def test_gt(self):
        """verify greater than fraction"""
        f13: Fraction = Fraction(1, 3)
        f45: Fraction = Fraction(4, 5)
        f128: Fraction = Fraction(12, 8)

        self.assertGreater(f45, f13)
        self.assertFalse(f13 > f128)

    def test_ge(self):
        """verify greater than or equal fraction"""
        f34: Fraction = Fraction(3, 4)
        f128: Fraction = Fraction(12, 8)
        f67: Fraction = Fraction(6, 7)

        self.assertGreaterEqual(f128, f34)
        self.assertFalse(f34 >= f67)
        self.assertTrue(f67 >= f67)
    
    
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)