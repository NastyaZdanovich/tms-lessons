class Rational:
    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator
        self.__normalise()

    @property
    def nominator(self):
        return self.__nominator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__nominator} / {self.__denominator}'

    def __mul__(self, other):
        new_nominator = self.__nominator * other.__nominator
        new_denominator = self.__denominator * other.__denominator
        return Rational(new_nominator, new_denominator)

    def __truediv__(self, other):
        new_nominator = self.__nominator * other.__denominator
        new_denominator = self.__denominator * other.__nominator
        return Rational(new_nominator, new_denominator)

    def __add__(self, other):
        common_denominator = self.__denominator * other.__denominator
        new_nominator1 = self.__nominator * other.__denominator
        new_nominator2 = self.__denominator * other.__nominator
        new_nominator = new_nominator1 + new_nominator2
        return Rational(new_nominator, common_denominator)

    def __sub__(self, other):
        common_denominator = self.__denominator * other.__denominator
        new_nominator1 = self.__nominator * other.__denominator
        new_nominator2 = self.__denominator * other.__nominator
        new_nominator = new_nominator1 - new_nominator2
        return Rational(new_nominator, common_denominator)

    def __eq__(self, other):
        return self.__nominator * other.__denominator == self.__denominator * other.__nominator

    def __ne__(self, other):
        return self.__nominator * other.__denominator != self.__denominator * other.__nominator

    def __ge__(self, other):
        return self.__nominator * other.__denominator >= self.__denominator * other.__nominator

    def __gt__(self, other):
        return self.__nominator * other.__denominator > self.__denominator * other.__nominator

    def __le__(self, other):
        return self.__nominator * other.__denominator <= self.__denominator * other.__nominator

    def __lt__(self, other):
        return self.__nominator * other.__denominator < self.__denominator * other.__nominator

    def __normalise(self):
        def gcd(a, b):
            while b > 0:
                c = a % b
                a = b
                b = c
            return a

        divisor = gcd(self.__nominator, self.__denominator)
        self.__nominator //= divisor
        self.__denominator //= divisor

        if self.__denominator < 0:
            self.__nominator *= -1
            self.__denominator *= -1


if __name__ == '__main__':
    assert (Rational(1, 2) * Rational(3, 6)) == Rational(1, 4)
    assert (Rational(-1, 2) / Rational(3, 6)) == Rational(-1, 1)
    assert (Rational(3, 4) + Rational(1, 7)) == Rational(25, 28)
    assert (Rational(1, 5) - Rational(2, 3)) == Rational(-7, 15)
    assert Rational(2, 4) == Rational(4, 8)
    assert Rational(1, 4) != Rational(1, 9)
    assert Rational(1, 4) >= Rational(4, 16)
    assert Rational(2, 3) > Rational(2, 15)
    assert Rational(1, -17) <= Rational(-1, 17)
    assert Rational(2, 5) < Rational(1, 2)
    assert Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100) == Rational(1573, 800)
