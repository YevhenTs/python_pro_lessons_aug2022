def add_str(text):
    def wrapped(cls):
        def my_function(*args, **kwargs):
            res = cls(*args, **kwargs)
            return text + res.__str__()
        return my_function
    return wrapped


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @add_str('Mr. ')
    def __str__(self):
        return f'{self.name} {self.surname}'


p1 = Person('Jack', 'Nicolson')
print(p1)