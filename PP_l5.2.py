import math


class Zero_Err(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"


class Ratio_Fract:

    def __init__(self, a: int, b: int):
        try:
            if a == 0 or b == 0:
                raise Zero_Err("Should not be 0!")
            if not isinstance(a, int) or not isinstance(b, int):
                raise ValueError
        except Zero_Err as err:
            print(err)
        except ValueError:
            print('Is not number!')
        self.a = a
        self.b = b

    def __str__(self):
        tmp = math.gcd(self.a, self.b)
        if tmp == 1:
            return f"{self.a}/{self.b}"
        else:
            self.a = self.a // tmp
            self.b = self.b // tmp
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
        s = self.a + other.a
        tmp1 = Ratio_Fract(s, self.b)
        if math.gcd(s, self.b) == 1:
            return tmp1
        else:
            a1 = s // math.gcd(s, self.b)
            b1 = self.b // math.gcd(s, self.b)
            tmp2 = Ratio_Fract(a1, b1)
            return tmp2

    def __sub__(self, other):
        self.c_denominator(other)
        subt = self.a - other.a
        tmp1 = Ratio_Fract(subt, self.b)
        if math.gcd(subt, self.b) == 1:
            return tmp1
        else:
            a1 = subt // math.gcd(subt, self.b)
            b1 = self.b // math.gcd(subt, self.b)
            tmp2 = Ratio_Fract(a1, b1)
            return tmp2

    def __mul__(self, other):
        a1 = self.a * other.a
        b1 = self.b * other.b
        tmp1 = Ratio_Fract(a1, b1)
        if math.gcd(a1, b1) == 1:
            return tmp1
        else:
            a2 = a1 // math.gcd(a1, b1)
            b2 = b1 // math.gcd(a1, b1)
            tmp2 = Ratio_Fract(a2, b2)
            return tmp2

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