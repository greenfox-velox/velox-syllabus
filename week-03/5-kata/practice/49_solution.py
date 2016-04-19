# create a Student class that stores grades and the student name
# it should have add_grade method
# also a get_average method

# create a Class class that contains students
# it should have an add_student method
# also a get_average method
# it should also have a get_names method

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

class Class:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
   #    summa = 0
   #    for student in self.students:
   #        summa += student.get_average()
   #    return summa / len(self.students)
        return sum(map(lambda s: s.get_average(), self.students)) / len(self.students)

    def get_names(self):
   #     names = []
   #     for student in self.students:
   #         names.append(student.name)
   #     return names
        return list(map(lambda s: s.name, self.students))



my_class = Class()

kati = Student('Kati')
kati.add_grade(5)
kati.add_grade(5)
kati.add_grade(4)
my_class.add_student(kati)
jozsi = Student('Jozsi')
jozsi.add_grade(3)
jozsi.add_grade(2)
jozsi.add_grade(1)
my_class.add_student(jozsi)
anti = Student('Antal')
anti.add_grade(5)
anti.add_grade(5)
anti.add_grade(3)
my_class.add_student(anti)

print(my_class.get_average())
print(my_class.get_names())









