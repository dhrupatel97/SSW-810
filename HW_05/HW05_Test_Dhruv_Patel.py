"""
Implementation of a test suite for testing the string function
"""

import unittest
from HW05_Dhruv_Patel import reverse, substring, find_second, get_lines

# PART 1

class ReverseTest(unittest.TestCase):

    def test_reverse(self) -> None:
        """testing reverse string"""

        self.assertEqual(reverse('naman'), 'naman')
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('dHruV'), 'VurHd')
        self.assertNotEqual(reverse('hey'), 'HEY')

# PART 2

class SubstringTest(unittest.TestCase):

    def test_substring(self) -> None:
        """testing substring function"""

        self.assertEqual(substring('ello', 'hello'), 1)
        self.assertEqual(substring('q', 'naman'), -1)
        self.assertEqual(substring('wa', 'software'), 4)
        self.assertNotEqual(substring('he' , "hello") , 1)

# PART 3

class FindSecondTest(unittest.TestCase):

    def test_find_second(self) -> None:
        """testing find_second function"""
        
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second('abba' , 'abbabb') , -1)
        self.assertTrue(find_second("iss" , "mississipi") , 4)
        self.assertNotEqual(find_second("abba" , "abbabba") , 2)

# PART 4

class GetLinesTest(unittest.TestCase):
    
    def test_get_lines(self) -> None:
        """ verify get_lines function"""

        file_name = 'E:/Stevens Institute of Technology/2nd Sem/SSW 810/Assignments/HW_05/Readme.txt'
        expect:list = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        unexpect:list = ['<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>']
        result:list = list(get_lines(file_name))

        self.assertEqual(result, expect)
        self.assertNotEqual(result , unexpect)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)