class Rectan:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return f'Width:{self.w} x Height:{self.h}'

    def rec_area(self):
        return self.w * self.h

    def __mul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        return self.rec_area() * other

    def __rmul__(self, other: int):
        return self.rec_area() * other

    def __add__(self, other):
        return self.rec_area() + other.rec_area()

    def __lt__(self, other):
        return self.rec_area() < other.rec_area()

    def __le__(self, other):
        return self.rec_area() <= other.rec_area()

    def __gt__(self, other):
        return self.rec_area() > other.rec_area()

    def __ge__(self, other):
        return self.rec_area() >= other.rec_area()

    def __eq__(self, other):
        return self.rec_area() == other.rec_area()

    def __ne__(self, other):
        return self.rec_area() != other.rec_area()


rect1 = Rectan(10, 6)
rect2 = 2 * rect1
print(rect2)
rect3 = Rectan(10, 6)
rect4 = rect1 + rect3
print(rect4)
