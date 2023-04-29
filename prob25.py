# practice prob 13
class University:
    name = "ABC University"
    numberOfStudents = 0
    admissionFee = 28000
    Library = 2000

    def __init__(self, n, i):
        self.stName = n
        self.stId = i

    def payment(self):
        return self.admissionFee + self.Library

    def __str__(self):
        return "Student Name: {}, ID: {}\nFee: {}".format(self.stName, self.stId, self.payment())


class CSE_dept(University):
    lab = 2750
    creditFee = 6600
    semesterFee = 7700

    def __init__(self, name, id, credit=6):
        super().__init__(name, id)
        self.credit = credit

    def payment(self):
        return self.admissionFee + self.Library + self.lab + (self.creditFee * self.credit) + self.semesterFee

    def payment_details(self):
        print(f"DETAILS: \nAdmission Fee: {self.admissionFee} \nLibrary Fee: {self.Library}\nSemester Fee: {self.semesterFee} \nPer Credit Fee: {self.creditFee} \nNumber of credits: {self.credit} \nLab Fee: {self.lab}")

    # def __str__(self):
    #     return "Student Name: {}, ID: {}\nFee: {}".format(self.stName, self.stId, self.payment() + (self.credit * 6600) + 7700 + 2750)


class PHR_dept(University):
    creditFee = 6600
    semesterFee = 11000

    def __init__(self, name, id, credit=9):
        super().__init__(name, id)
        self.credit = credit

    def payment(self):
        return self.admissionFee + self.Library + (self.creditFee * self.credit) + self.semesterFee

    def payment_details(self):
        print(
            f"DETAILS: \nAdmission Fee: {self.admissionFee} \nLibrary Fee: {self.Library}\nSemester Fee: {self.semesterFee} \nPer Credit Fee: {self.creditFee} \nNumber of credits: {self.credit} ")


c1 = CSE_dept("Mary", "5678")
print(c1)
c1.payment_details()
print("===========================")
p1 = PHR_dept("Simon", "91011")
print(p1)
p1.payment_details()
# print("===========================")
# c2 = CSE_dept("Adam", "1234", 12)
# print(c2)
# c2.payment_details()
# print("===========================")
# p2 = PHR_dept("David", "121314", 15)
# print(p2)
# p2.payment_details()
# print("===========================")
# print("Total Number of Students:", University.numberOfStudents)
# print("Total University Revenue:", (c1 + c2) + (p1 + p2))
# print("===========================")
# print("Due to the pandemic, admission and library fees have been reduced for all departments. ")
# University.admissionFee -= 1000
# University.Library -= 100
# print("The credit, semester and lab fees have been reduced for the CSE department. ")
# CSE_dept.PerCreditFee -= 100
# CSE_dept.SemesterFee -= 100
# CSE_dept.LabFee -= 100
# print("The credit and semester fees have been reduced for the PHR department.\n ")
# PHR_dept.PerCreditFee -= 100
# PHR_dept.SemesterFee -= 1000
# print(c1)
# print(p1)
# print(c2)
# print(p2)
# print("===========================")
# print("Total Number of Students:", University.numberOfStudents)
# print("Total University Revenue:", (c1 + c2) + (p1 + p2))
