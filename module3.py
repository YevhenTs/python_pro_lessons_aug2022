import module2


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

    def add_student(self, student: module2.Student):
        try:
            if len(self.students) >= Group.MAX_STUDENTS:
                raise MaxStudentsError('Too many student in group!')
        except MaxStudentsError as err:
            print(err)

        for item in self.students:
            if item == student:
                return -2

        self.students.append(student)

    def del_student(self, student: module2.Student):
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