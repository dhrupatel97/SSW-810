"""
Implement some functions on python containers
"""

from typing import List, Any, Dict, Tuple, Set, DefaultDict, Counter
from collections import defaultdict

# PART 1
# PART 1.1

def anagrams_lst(str1: str, str2: str) -> bool:
    """check two string are anagram or not"""

    lst_str1 = list(str1)
    lst_str2 = list(str2)

    lst_str1.sort()
    lst_str2.sort()

    if lst_str1 == lst_str2:
        return True
    else:
        return False

# PART 1.2

def anagrams_dd(str1: str, str2: str):
    """checking anagram using defaultDictionary"""

    dd: DefaultDict[str, int] = defaultdict(int)
    
    for i in str1:
        dd[i] += 1
    
    for j in str2:
        dd[j] -= 1
    
    return all(k == 0 for k in dd.values())

# PART 1.3

def anagrams_cntr(str1: str, str2: str) -> bool:
    """anagram using counter"""

    return (Counter(str1.lower()) == Counter(str2.lower()))

# PART 2

def covers_alphabet(sentence: str) -> bool:
    """checking for at least one instance of every character in given input"""

    sample: str = 'abcdefghijklmnopqrstuvwxyz'
    return (set(sentence.lower()) >= set(sample))

# PART 3

def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """web analysis function"""

    dd: DefaultDict[str, str] = defaultdict(set)

    [dd[v].add(k) for k,v in weblogs]
    
    return sorted([(k, sorted(v)) for k, v in dd.items()])

    