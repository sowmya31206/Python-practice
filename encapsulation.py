class Student:
    def __init__(self):
        self.__marks = 90

    def display(self):
        print(self.__marks)

student = Student()
student.display()