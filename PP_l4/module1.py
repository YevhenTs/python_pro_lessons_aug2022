class Person:
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year

    def __str__(self):
        return f'{self.surname} {self.name} Year: {self.year}'