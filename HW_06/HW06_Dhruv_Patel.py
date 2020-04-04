"""
Implementating some functions on List and its properties
"""

from typing import List, Any, Optional

# PART 1

def list_copy(l: List[Any]) -> List[Any]:
    """copy elements from list 1 to list 2"""

    return [item for item in l]

# PART 2 

def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """find the common elements"""

    return [item for item in l1 for i in l2  if item == i]

# PART 3

def list_difference(l1: List[Any] , l2: List[Any]) -> List[Any]:
    """find the elements not present in l2 bu tpresent in l1"""

    return [i for i in l1 if i not in l2]

# PART 4

def remove_vowels(string: str) -> str:
    """remove the words starting from a vowel"""

    return " ".join([i for i in string.split() if i[0] not in 'aeiouAEIOU'])


# PART 5

def check_pwd(password: str) -> bool:
    """check the password for 3 condition"""

    upper_case: int = 0

    for y in password:
        if y.isupper():
            upper_case += 1
    
    if upper_case >= 2:
        return any(u.islower() for u in password) and password[0].isdigit()
    else:
        return False

    # return len(pwd) >= 4 \
    #         and sum([1 for c in pwd if c.upper()]) >= 2 \
    #         and sum([1 for c in pwd if c.upper()]) >= 1 \
    #         and pwd[0].isdigit()


# PART 6

class Queue:
    """ Providing queue functionality"""

    def __init__(self) -> None:
        self.queue: List[str] = list()

    def add(self, name: str) -> None:
        """adding new name to queue"""

        self.queue.append(name)
    
    def get_next(self) -> None:
        """pop the first customer in queue"""

        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None
    
    def waiting(self) -> None:
        """return the queue order"""

        return self.queue

class DonutQueue:

    def __init__(self) -> None:
        self.vip_q: Queue = Queue()
        self.stand_q: Queue = Queue()

    def arrive(self, name: str, vip: bool) -> None:
        """add the new name to queue"""

        if vip:
            self.vip_q.add(name)
        else:
            self.stand_q.add(name)

    def next_customer(self) -> Optional[str]:
        """pop the next customer"""

        customer:str = self.vip_q.get_next()
        if customer is None:
            customer = self.stand_q.get_next()
        return customer

    def waiting(self) -> Optional[str]:
        """get the order of customer"""

        vips: List[str] = self.vip_q.waiting()
        standard: List[str]= self.stand_q.waiting()
        all:List[str] = vips + standard
        return ", ".join(all)