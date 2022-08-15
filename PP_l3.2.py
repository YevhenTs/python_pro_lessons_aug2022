import random


class Person:
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year

    def __str__(self):
        return f'{self.surname} {self.name} Year: {self.year}'


class Student(Person):
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
        return self.surname == other.surname and self.name == other.name and self.year == other.year

    def __str__(self):
        return f'Name: {self.name} / Surname: {self.surname} / Birth year: {self.year} / {self.add_score()} score / {self.city}'


class MaxStudentsError(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}\n{super().__str__()}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, course):
        self.title = course.rjust(48, ' ')
        self.students = []

    def add_student(self, student: Student):
        try:
            if len(self.students) >= Group.MAX_STUDENTS:
                raise MaxStudentsError('Too many student in group!')
        except MaxStudentsError as err:
            print(err)

        for item in self.students:
            if item == student:
                return -2

        self.students.append(student)

    def del_student(self, student: Student):
        self.students.remove(student)

    def find_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student

    def __str__(self):
        res = '\n'
        res += f'{self.title}\n'
        res += '\n'.join(map(str, self.students))
        return res



per1 = Student('John', 'Johnov', '1992')
per2 = Student('Sam', 'Samov', '1991')
per3 = Student('Chris', 'Chrisov', '1992')
per4 = Student('Jordan', 'Jordanov', '1991')
per5 = Student("Jim", "Jimov", '1993')
per6 = Student('Yevhen', 'Yevhenovich', '1992')
per7 = Student('Taras', 'Tarasovich', '1990')
per8 = Student('Vadim', 'Vadimovich', '1992')
per9 = Student('Ihor', 'Ihorovich', '1990')
per10 = Student('Oleh', 'Olehovich', '1992')
per11 = Student('Oleh', 'Olehovich', '1992')
per12 = Student('Oleh1', 'Olehovich1', '1992')

gr_avia = Group('Aircraft Maintenance Faculty\n')
gr_avia.add_student(per1)
gr_avia.add_student(per2)
gr_avia.add_student(per3)
gr_avia.add_student(per4)
gr_avia.add_student(per5)
gr_avia.add_student(per6)
gr_avia.add_student(per7)
gr_avia.add_student(per8)
gr_avia.add_student(per9)
gr_avia.add_student(per10)
gr_avia.add_student(per11)
gr_avia.add_student(per12)


print(gr_avia)
print('Student absent:', gr_avia.find_student('Johnov'))