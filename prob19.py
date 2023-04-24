# practice problem 06
class Student:
    student = 0
    cseCount = 0
    bbaCount = 0

    def __init__(self, name, dept):
        Student.student += 1
        print(f"Creating Student Number: {Student.student}")
        self.name = name
        self.dept = dept

    def individualInfo(self):
        if (self.dept == "CSE"):
            Student.cseCount += 1
        else:
            Student.bbaCount += 1
        print(f"{self.name} is from {self.dept} department.")
        print(
            f"Serial of {self.name} among all students is: {Student.student}")
        if (self.dept == "CSE"):
            print(
                f"Serial of {self.name} in {self.dept} department is: {Student.cseCount}")
        else:
            print(
                f"Serial of {self.name} in {self.dept} department is: {Student.bbaCount}")

    def totalInfo(self):
        print(f"Total Number of Student: {Student.student}")
        print(f"Total Number of CSE Student: {self.cseCount}")
        print(f"Total Number of BBA Student: {self.bbaCount}")


s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')


s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')


s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')


s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()
