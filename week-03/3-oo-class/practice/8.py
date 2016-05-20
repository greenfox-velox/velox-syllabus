class Person:
    def __init__(self, first_name, last_name):
        self.f_n = first_name
        self.l_n = last_name

    def greet(self):
        print('Hi I am: ' + self.f_n + ' ' + self.l_n)


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def add_grade(self, new_grade):
        self.grades.append(new_grade)

    def salute(self):
        self.greet()
        summa = 0
        for grade in self.grades:
            summa += grade
        print(summa / len(self.grades))

adorjan = Student('Adorjan', 'Cseh-Szombathy')

adorjan.add_grade(1)
adorjan.add_grade(3)
adorjan.salute()
