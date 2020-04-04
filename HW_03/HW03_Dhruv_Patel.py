"""
Implement a fraction calculator that is capable for addition, subtraction, multiplication, division

"""

class Fraction:
    """
    supports addition, subtraction, multiplication, division
    """

    def __init__(self, numerator: float, denominator: float) -> None:
        """
        store numerator and denominator
        raise a ValueError if denominator is zero
        """
        self.numerator: float = numerator
        self.denominator: float = denominator

        if self.denominator == 0:
            raise ZeroDivisionError('Denominator is Zero')

    def __str__(self) -> str:
        """return a string to display fraction"""

        return f"{self.numerator} / {self.denominator}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """addition
        return a new fraction
        """

        numerator: float = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator: float = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """subtraction
        return a new fraction
        """

        numerator: float = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator: float = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """multiplication
        return a new fraction
        """

        numerator: float = self.numerator * other.numerator
        denominator: float = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ division
        return a new fraction
        """
        numerator: float = (self.numerator * other.denominator)
        denominator: float = (self.denominator * other.numerator)

        return Fraction(numerator, denominator)

    def __eq__(self, other: "Fraction") -> bool:
        """comparing fraction
        return true or false
        """

        lhs: float = self.numerator * other.denominator
        rhs: float = self.denominator * other.numerator

        if lhs == rhs:
            return True
        else:
            return False

    def __ne__(self, other: "Fraction") -> bool:
        """ Not equal comparision"""

        if self.numerator / self.denominator != other.numerator / other.denominator:
            return True
        else:
            return False

    def __lt__(self, other: "Fraction") -> bool:
        """less than comparision"""

        if self.numerator / self.denominator < other.numerator / other.denominator:
            return True
        else:
            return False
        
    def __le__(self, other: "Fraction") -> bool:
        """less than or equal to comparision"""

        if self.numerator / self.denominator <= other.numerator / other.denominator:
            return True
        else:
            return False
    
    def __gt__(self, other: "Fraction") -> bool:
        """greater than comparision"""

        if self.numerator / self.denominator > other.numerator / other.denominator:
            return True
        else:
            return False
    
    def __ge__(self, other: "Fraction") -> bool:
        """greater than or equal to comparision"""

        if self.numerator / self.denominator >= other.numerator / other.denominator:
            return True
        else:
            return False


def get_number() -> float:
    """
    get input from user 
    check for invalid input
    """

    while True:
        n1: str = input("Please provide a number: ")
        try:
            return float(n1)
        except ValueError:
            print(n1, 'is not a valid number. Please try again...')


def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """
    perform operation
    call the function for the operation selected
    """

    result: Fraction
    okay: bool = True

    if operator == '+':
        result = f1 + f2
    elif operator == '-':
        result = f1 - (f2)
    elif operator == '*':
        result = f1 * (f2)
    elif operator == '/':
        try:
            result = f1 / (f2)
        except ZeroDivisionError:
            print("Denominator can't be Zero")
    elif operator == '==':
        result = (f1 == (f2))
    elif operator == '!=':
        result = (f1 != f2)
    elif operator == '<':
        result = (f1 < f2)
    elif operator == '<=':
        result = (f1 <= f2)
    elif operator == '>':
        result = (f1 > f2)
    elif operator == '>=':
        result = (f1 >= f2)
    else:
        print(f"Sorry, Operator '{operator}' is not recognized.")
        okay = False

    if okay == True:
        print(f"[{f1}] {operator} [{f2}] = [{result}]")


def main() -> None:
    """
    fraction calculation
    """

    print("Welcome to Fraction Calculator!!")
    print("Fraction 1: ")
    n1: float = get_number()
    d1: float = get_number()

    operator: str = input("Operation (+,-,*,/,==,!=,<,<=,>,>=): ")

    print("Fraction 2: ")
    n2: float = get_number()
    d2: float = get_number()

    f1: Fraction = Fraction(n1, d1)
    f2: Fraction = Fraction(n2, d2)

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    main()
