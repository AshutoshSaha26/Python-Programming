from fractions import Fraction as PyFraction  
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
    def __init__(self, *args):
        if len(args) == 1:
            frac = PyFraction(args[0])
            self.numerator = frac.numerator
            self.denominator = frac.denominator
        elif len(args) == 2:
            self.numerator = args[0]
            if args[1] == 0:
                raise ValueError("Denominator cannot be zero.")
            self.denominator = args[1]
        else:
            raise ValueError("Invalid number of arguments")
    def display_fraction(self):
        print(f"{self.numerator}/{self.denominator}")
if __name__ == "__main__":
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction("5/6")
    fraction3 = Fraction(7, 2)
    fraction1.display_fraction()
    fraction2.display_fraction()
    fraction3.display_fraction()
