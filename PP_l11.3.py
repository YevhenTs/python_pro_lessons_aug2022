from datetime import datetime


class MyDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        self.value = value
        with open("start_set.txt", 'a') as g:
            print(f'Set time: {datetime.now()}, Age: {self.value}', file=g)

    def __delete__(self, instance_self):
        raise AttributeError("You can't delete field")


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    age = MyDescriptor(32)


p1 = Person('Jack', 'Nicolson')
p1.age = 34
