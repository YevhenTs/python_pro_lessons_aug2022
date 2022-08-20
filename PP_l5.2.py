import math


class Zero_Err(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"


class Ratio_Fract:

    def __init__(self, a: int, b: int):
        if b == 0:
            raise Zero_Err()
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError()

        tmp = math.gcd(a, b)
        self.a = a // tmp
        self.b = b // tmp

    def __str__(self):
        return f"{self.a}/{self.b}"

    def c_denominator(self, other):
        if self.b != other.b:
            self.a = self.a * other.b
            other.a = other.a * self.b
            self.b = self.b * other.b
            other.b = self.b
        return self, other

    def __add__(self, other):
        self.c_denominator(other)
        a = self.a + other.a
        return Ratio_Fract(a, self.b)

    def __sub__(self, other):
        self.c_denominator(other)
        a = self.a - other.a
        return Ratio_Fract(a, self.b)

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return Ratio_Fract(a, b)

    def __le__(self, other):
        return self.a <= other.a

    def __ge__(self, other):
        return self.a >= other.a


dr1 = Ratio_Fract(10, 20)
dr2 = Ratio_Fract(5, 40)

print(dr1, dr2)

print(dr1 * dr2)
print(dr1 + dr2)
print(dr1 - dr2)