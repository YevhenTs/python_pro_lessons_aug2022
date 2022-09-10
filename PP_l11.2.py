class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Box x = {self.x} y = {self.y} z = {self.z}'

    def __setattr__(self, attr_name, attr_value):
        if not isinstance(attr_value, int):
            raise TypeError()
        self.__dict__[attr_name] = attr_value


box1 = Box(3, 3, 3)
print(box1)
box2 = Box(3, 3, 3.5)
print(box2)