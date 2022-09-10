class Meta(type):

    def __new__(class_type, class_name, supers, dict):
        with open('meta_file.txt', 'w') as g:
            print(class_name + "\n", file=g)
            for i in dict:
                print(str(i) + "\n", file=g)
        return type.__new__(class_type, class_name, supers, dict)


class Cat(metaclass=Meta):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Cat: name ={self.name}, age = {self.age}'


cat1 = Cat("Fin", 4)
