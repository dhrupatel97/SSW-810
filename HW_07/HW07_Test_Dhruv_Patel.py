"""
Building a test suite for testing python containers functions
"""

import unittest
from HW07_Dhruv_Patel import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer
from typing import List, Tuple

# PART 1

#PART 1.1

class AnagramListTest(unittest.TestCase):

    def test_anagram_lst(self) -> None:
        """testing anagram list function"""

        self.assertTrue(anagrams_lst('iceman', 'cinema'))
        self.assertFalse(anagrams_lst('icecream', 'cinema'))
        self.assertTrue(anagrams_lst('EduCatiOn', 'CautiOnEd'))
        self.assertTrue(anagrams_lst('',''))

# PART 1.2

class AnagramDDList(unittest.TestCase):

    def test_anagram_dd(self) -> None:
        """testing anagram dd function"""

        self.assertTrue(anagrams_dd('iceman', 'cinema'))
        self.assertFalse(anagrams_dd('icecream', 'cinema'))
        self.assertTrue(anagrams_dd('EduCatiOn', 'CautiOnEd'))
        self.assertTrue(anagrams_lst('',''))

# PART 1.3

class AnagramCntrTest(unittest.TestCase):

    def test_anagram_cntr(self) -> None:
        """testing anagram counter function"""

        self.assertTrue(anagrams_dd('iceman', 'cinema'))
        self.assertFalse(anagrams_dd('icecream', 'cinema'))
        self.assertTrue(anagrams_dd('EduCatiOn', 'CautiOnEd'))
        self.assertTrue(anagrams_lst('',''))

# PART 2

class CoversAlphabetTest(unittest.TestCase):

    def test_covers_alphabet(self) -> None:
        """testing covering alphabet"""

        self.assertTrue(covers_alphabet('AbCdefghiJklomnopqrStuvwxyz'))
        self.assertTrue(covers_alphabet('The quick, brown, fox; jumps over the lazy dog!'))
        self.assertFalse(covers_alphabet('xyz'))
        self.assertTrue(covers_alphabet('aabbcdefghijklmnopqrstuvwxyzzabc'))

# PART 3

class WebAnalyzerTest(unittest.TestCase):

    def test_web_analyzer(self) -> None:
        """testing web analyzer function"""

        weblogs: List[Tuple[str, str]] = [
        ('Nanda', 'google.com'), ('Maha', 'google.com'), 
        ('Fei', 'python.org'), ('Maha', 'google.com'), 
        ('Fei', 'python.org'), ('Nanda', 'python.org'), 
        ('Fei', 'dzone.com'), ('Nanda', 'google.com'), 
        ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
        ('dzone.com', ['Fei']), 
        ('google.com', ['Maha', 'Nanda']), 
        ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)