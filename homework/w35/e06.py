def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def print(self) -> None:
        print(f"{self.numerator}/{self.denominator}")

    def reduce(self) -> None:
        d = gcd(self.numerator, self.denominator)
        self.numerator /= d
        self.denominator /= d

n = Fraction(4, 2)
n.print()
n.reduce()
n.print()
