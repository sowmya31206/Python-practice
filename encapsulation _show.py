class Student:
    def __init__(self):
        self.__marks = 90

    def show(self):
        return self.__marks

s = Student()

print(s.show())