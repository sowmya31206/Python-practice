class Student:
    def __init__(self):
        self.__marks = 90

    def update(self, marks):
        self.__marks = marks

    def show(self):
        print(self.__marks)

s = Student()

s.update(95)

s.show()