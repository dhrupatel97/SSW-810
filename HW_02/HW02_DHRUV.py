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

        if denominator == 0:
            raise ValueError('Denominator is Zero')

    def __str__(self) -> str:
        """return a string to display fraction"""

        return f"{self.numerator} / {self.denominator}"

    def plus(self, other: "Fraction") -> "Fraction":
        """addition
        return a new fraction
        """

        numerator: float = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator: float = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def minus(self, other: "Fraction") -> "Fraction":
        """subtraction
        return a new fraction
        """

        numerator: float = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator: float = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def times(self, other: "Fraction") -> "Fraction":
        """multiplication
        return a new fraction
        """

        numerator: float = self.numerator * other.numerator
        denominator: float = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def divide(self, other: "Fraction") -> "Fraction":
        """ division
        return a new fraction
        """
        numerator: float = (self.numerator * other.denominator)
        denominator: float = (self.denominator * other.numerator)

        return Fraction(numerator, denominator)

    def equal(self, other: "Fractioin") -> bool:
        """comparing fraction
        rerturn true or false
        """

        lhs: float = self.numerator * other.denominator
        rhs: float = self.denominator * other.numerator

        if lhs == rhs:
            return True
        else:
            return False


def test_suite() -> None:
    """ We'll see a better testing approach next week but here's a start.
        Note that each statement includes the result of the computation plus 
        the expected answer to help to quickly identify if everything works properly.
    """
    print("Running Test Suite: ")
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)
    f44: Fraction = Fraction(4, 4)

    print(f"[{f12}] + [{f34}] = {f12.plus(f34)} [Expected: 10/8]")
    print(f"[{f128}] - [{f68}] = {f128.minus(f68)} [Expected: 48/64]")
    print(f"[{f32}] * [{f912}] = {f32.times(f912)} [Expected: 27/24]")
    print(f"[{f68}] / [{f32}] = {f68.divide(f32)} [Expected: 12/24]")
    print(f"[{f12}] + [{f34}] + [{f44}] = [{f12.plus(f34).plus(f44)}] [Expected: 72/32]")

    print("__str__ for [1/2] = ", str(f12))
    print("__str__ for [6/8] = ", str(f68))
    print("__str__ for [12/8] = ", str(f128))


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
        result = f1.plus(f2)
    elif operator == '-':
        result = f1.minus(f2)
    elif operator == '*':
        result = f1.times(f2)
    elif operator == '/':
        try:
            result = f1.divide(f2)
        except ZeroDivisionError:
            print("Denominator can't be Zero")
    elif operator == '==':
        result = f1.equal(f2)
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

    operator: str = input("Operation (+,-,*,/,==): ")

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
    test_suite()
    print("Now Running Main: ")
    main()
