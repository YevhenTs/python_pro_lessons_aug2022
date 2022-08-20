import module1
import random


class Student(module1.Person):
    def __init__(self, name, surname, year, city='Kiev'):
        super().__init__(name, surname, year)
        self.city = city

    def add_score(self, score=None):
        sc = []
        for n in range(2):
            sc.append(random.randint(6, 9))
            score = ''.join(map(str, sc))
        return score

    def __eq__(self, other):
        return (self.surname, self.name, self.year) == (other.surname, other.name, other.year)

    def __str__(self):
        return f'Name: {self.name} / Surname: {self.surname} / Birth year: {self.year} / {self.add_score()} score / {self.city}'