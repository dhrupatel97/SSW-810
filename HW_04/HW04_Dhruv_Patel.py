"""
Implementation of following function: 
1. counting vowels
2.find the last occurence 
3. Enumerator function
"""

import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator

# PART 1

def count_vowels(s: str) -> int:
    ''' return the number of vowels in the string s '''

    word: str = s.lower()
    vowel_list: str = ['a', 'e', 'i', 'o', 'u']
    count: int = 0

    for char in word:
        if char in vowel_list:
            count = count + 1
    
    return count

    #pythonic function
    # return sum(1 for c in s.lower() if c in [a', 'e', 'i', 'o', 'u'])

# PART 2
    
def find_last(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    i: int = 0
    f: int  = len(seq)
    offset: int = None

    while i < f:
        if target == seq[i]:
            offset = i
        i = i + 1

    if offset == None:
        return 0
    else:
        return offset
  
# PART 3 is Fraction.simplify()

# PART 4
def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """

    for i in seq:
        yield seq.index(i), i
