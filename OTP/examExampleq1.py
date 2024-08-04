class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Öğrencinin adı : {self.name}, yaşı : {self.age}")


class Student(Person):
    def __init__(self,name,age,section):
        Person.__init__(self,name,age)
        self.section = section

    def display_student(self):
        print(f"Öğrencinin adı : {self.name}, yaşı : {self.age}, bölümü : {self.section}")


p1 = Person("Furkan", 19)
Person.display(p1)
ogr1 = Student("Akyel", 20, "BM")
Student.display_student(ogr1)