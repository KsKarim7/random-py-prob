# practice problem10
class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"
# Write your code here


class CSEStudent(Student):
    def __init__(self, name, id, sem):
        super().__init__(name, id)
        self.sem = sem
        self.dict = {}
        self.gpa = 0

    def Details(self):
        return f"{super().Details()}Current semester: {self.sem}"

    def addCourseWithMarks(self, *args):
        count = 1
        for i in range(0, len(args), 2):
            if (args[count] >= 85):
                self.dict[args[i]] = 4.0
            elif (args[count] <= 84 and args[count] >= 80):
                self.dict[args[i]] = 3.3
            elif (args[count] <= 79 and args[count] >= 70):
                self.dict[args[i]] = 3.0
            elif (args[count] <= 69 and args[count] >= 65):
                self.dict[args[i]] = 2.3
            elif (args[count] <= 64 and args[count] >= 57):
                self.dict[args[i]] = 2.0
            elif (args[count] <= 56 and args[count] >= 55):
                self.dict[args[i]] = 1.3
            elif (args[count] <= 54 and args[count] >= 50):
                self.dict[args[i]] = 1
            else:
                self.dict[args[i]] = 0
            count += 2
        print(self.dict)
    # def showGPA(self):


Bob = CSEStudent("Bob", "20301018", "Fall 2020")
Carol = CSEStudent("Carol", "16301814", "Fall 2020")
Anny = CSEStudent("Anny", "18201234", "Fall 2020")
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111", 83.5, "CSE230", 73.0, "CSE260", 92.5)
