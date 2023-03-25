# class Student:
#     def __init__(self, name='Just a student', dept='nothing'):
#         self.__name = name
#         self.__department = dept
#     def set_department(self, dept):
#         self.__department = dept
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name = name
#     def __str__(self):
#         return 'Name: '+self.__name+' Department: '+self.__department


# #write your code here

# print(BBA_Student())
# print(BBA_Student('Humpty Dumpty'))
# print(BBA_Student('Little Bo Peep'))

# Output:
# Name: default Department: BBA
# Name: Humpty Dumpty Department: BBA
# Name: Little Bo Peep Department: BBA

class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept

    def set_department(self, dept):
        self.__department = dept

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department


class BBA_Student:
    def __init__(self, name='default', dept="BBA"):
        self.s = Student(name, dept)
        self.s.set_department(dept)
        self.s.set_name(name)
        l = self.s.__str__()
        print(l)
    # s.set_name(name)
    # s.__str__()


print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))
