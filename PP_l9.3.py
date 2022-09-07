def file_decor(f):
    def my_function(arg):
        res = f(arg)
        with open('person.txt', 'w') as g:
            print(res, file=g)
        return res
    return my_function


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.class_name = self.__class__.__name__

    @file_decor
    def __str__(self):
        return f'{self.surname} {self.name}'


p_1 = Person('Jack', 'Nicolson')


print(p_1)
