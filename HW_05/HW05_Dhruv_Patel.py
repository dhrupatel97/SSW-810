"""
This file contains functions on strings, slices, working with files 
"""

from typing import Any, List, Optional, Sequence, Iterator, IO

# PART 1

def reverse(s: str) -> str:
    """reverse a given string"""

    char_lst: List[str] = []

    for i in range(0, len(s)):
        char_lst.append(s[len(s) - 1 - i])

    char_lst = ''.join(char_lst)

    return char_lst


# PART 2

def substring(target: str, s: str) -> int:
    """check for the substring present and return the offset of the beginning"""

    start: int = 0
    end: int = 0

    while start < len(s):
        if s[start+end] != target[end]:
            start += 1
            end = 0
            continue
        end += 1
        
        if end == len(target):
            return start
    return -1


# PART 3

def find_second(target: str, string: str) -> int:
    """find the second occurence of the substring"""

    return string.find(target, string.find(target) + 1)


# PART 4

def get_lines(path: str) -> Iterator[str]:
    """return valid line on reading from a file"""

    try:
        fp: IO = open(path, 'r')
    except FileNotFoundError:
        print(f"Cannot open {path}")
    else:
        with fp:
            for line in fp:
                line = line.rstrip()

                while line.endswith('\\'):
                    line = line[:-1] + fp.readline().strip('\n')

                if '#' in line:
                    if line[0] != '#':
                        yield line[:line.find('#')]
                    else:
                        continue
                else:
                    yield line

