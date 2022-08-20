import module2
import module3


per1 = module2.Student('John', 'Johnov', '1992')
per2 = module2.Student('Sam', 'Samov', '1991')
per3 = module2.Student('Chris', 'Chrisov', '1992')
per4 = module2.Student('Jordan', 'Jordanov', '1991')
per5 = module2.Student("Jim", "Jimov", '1993')
per6 = module2.Student('Yevhen', 'Yevhenovich', '1992')
per7 = module2.Student('Taras', 'Tarasovich', '1990')
per8 = module2.Student('Vadim', 'Vadimovich', '1992')
per9 = module2.Student('Ihor', 'Ihorovich', '1990')
per10 = module2.Student('Oleh', 'Olehovich', '1992')
per11 = module2.Student('Oleh', 'Olehovich', '1992')
per12 = module2.Student('Oleh1', 'Olehovich1', '1992')

gr_avia = module3.Group('Aircraft Maintenance Faculty\n')
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