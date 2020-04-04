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

    def simplify(self) -> "Fraction":
        """simplify fraction i.e. reducing to its lowest form"""

        num: float = abs(self.numerator)
        deno: float = abs(self.denominator)

        HCF: float = -1

        smaller: float = None

        if num < deno:
            smaller = num
        else:
            smaller = deno
        
        i: float = smaller

        while i > 0:
            if num % i == 0 and deno % i == 0:
                HCF = i
                return f"{self.numerator/HCF} / {self.denominator/HCF}"
            else:
                i = i - 1
            

        



