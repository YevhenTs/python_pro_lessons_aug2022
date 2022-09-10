class MyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError("Field is read-only")

    def __delete__(self, instance_self):
        raise AttributeError("You can't delete field")


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    age = MyDescriptor(31)


p1 = Person('Jack', 'Nicolson')
print(p1)
print(p1.age)
p1.age = 32