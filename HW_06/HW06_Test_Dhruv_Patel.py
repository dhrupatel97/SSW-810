"""
Building a test suite for testing lst functions
"""

import unittest
from HW06_Dhruv_Patel import check_pwd, list_copy, list_difference, list_intersect, remove_vowels, DonutQueue, Queue

# PART 1

class ListCopyTest(unittest.TestCase):

    def test_list_copy(self) -> None:
        """testing list_copy function"""

        self.assertEqual(list_copy([1, 4, 5, 6]), [1, 4, 5, 6])
        self.assertEqual(list_copy([5, 6, 4, 'a']), [5, 6, 4, 'a'])
        self.assertEqual(list_copy([]), [])
        self.assertNotEqual(list_copy([2, 4, 5, 5]), [2, 4, 5])

# PART 2

class ListIntersectTest(unittest.TestCase):

    def test_list_intersect(self) -> None:
        """testing list_intersect function"""

        self.assertTrue(list_intersect([1, 2, 3], [1, 2, 4]) == [1, 2])
        self.assertEqual(list_intersect([2, 5, 7, 3], [2, 5, 7, 3]), [2, 5, 7, 3])
        self.assertEqual(list_intersect([3, 4, 5], [1, 7, 8]), [])
        

# PART 3

class ListDifferenceTest(unittest.TestCase):

    def test_list_difference(self) -> None:
        """testing list_difference function"""

        self.assertTrue(list_difference([1, 2, 3], [1, 2, 4]) == [3])
        self.assertTrue(list_difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3])
        self.assertEqual(list_difference(['e', 2, 'l'],['e', 6, 8]), [2, 'l'])

# PART 4

class RemoveVowelsTest(unittest.TestCase):

    def test_remove_vowels(self) -> None:
        """testing remove vowels function"""

        self.assertTrue(remove_vowels("Jan is my best friend") == "Jan my best friend")
        self.assertTrue(remove_vowels("Amy is my favorite daughter") == "my favorite daughter")
        self.assertEqual(remove_vowels("Hello World"), "Hello World")
        self.assertNotEqual(remove_vowels("amy is my friend"), "Amy Is my friend")

# PART 5

class CheckPwdTest(unittest.TestCase):

    def test_check_pwd(self) -> None:
        """testing check pwd function"""

        self.assertFalse(check_pwd("dh90YU"))
        self.assertTrue(check_pwd("7SWnj"))
        self.assertFalse(check_pwd("lsjhflskjh"))
        self.assertFalse(check_pwd('4fgtI'))
        self.assertTrue(check_pwd('45TYVCBGFoihooiho'))
        self.assertFalse(check_pwd('434iuoiuF'))

# PART 6

class DonutQueueTest(unittest.TestCase):

    def test_queue(self):
        """testing donut_queue function"""

        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)