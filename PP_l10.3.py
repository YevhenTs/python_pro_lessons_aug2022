class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Box x = {self.x} y = {self.y} z = {self.z}'

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def sum(a, b):
        return a.volume() + b.volume()


box1 = Box(3, 3, 3)
box2 = Box(3, 3, 3)

print(Box.sum(box1, box2))