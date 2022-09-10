list1 = []


def add_class(cls):
    list1.append(cls)
    return cls


@add_class
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'


print(list1)