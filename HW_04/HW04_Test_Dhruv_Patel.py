
import random
import unittest
from typing import Iterator, List, Tuple
from HW04_Dhruv_Patel import count_vowels, find_last, my_enumerate
# PART 1
    
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        """ testing count vowels """

        self.assertEqual(count_vowels('hEllo wOrld'), 3)
        self.assertTrue(count_vowels('DhrUv'), 1)
        self.assertEqual(count_vowels('Jehlum'), 2)
        self.assertNotEqual(count_vowels('dhrV'), 2)
        self.assertNotEqual(count_vowels('NaMaN'), 3)
        
# PART 2
    
class FindLastTest(unittest.TestCase):
    def test_find_last(self) -> None:
        """ testing find_last """

        self.assertEqual(find_last(33, [42, 33, 33, 45, 33, 33]), 5)
        self.assertTrue(find_last('l', ['h','l','k','l','i','o']), 3)
        self.assertEqual(find_last(4, [1, 3, 5, 6, 8]), 0)
        self.assertNotEqual(find_last(5, [54, 65, 43 , 4, 5, 5]), 4)
        self.assertEqual(find_last('l', 'apPle'), 3)

# PART 4

class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """

        self.assertEqual(list(my_enumerate('python')), list(enumerate('python')))
        self.assertEqual(list(my_enumerate(['m','I','K','e'])), list(enumerate(['m','I','K','e'])))
        self.assertFalse(list(my_enumerate('heyy!'))== list(enumerate("hello!")))
        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)