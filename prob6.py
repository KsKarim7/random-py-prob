# ### DRIVER CODE ####
# Usis_app=Usis()

# Araf = Faculty("Araf",1010,99)
# Usis_app.AddTeacher(Araf)
# print("#######################################\n")

# Asif = Faculty("Asif",1001,25)
# Usis_app.AddTeacher(Asif)
# print("########################################\n")

# student1=Student("Tamim",2221010,19,3.5)
# Usis_app.AddStudent(student1)
# print("########################################\n")

# student2=Student("Kayes",2221011,19,3.25)
# Usis_app.AddStudent(student2)
# print("########################################\n")

# student1.addCourse("CSE110",3.3,"ENG101",3.7,"MAT092",3.3)
# print("student1 Courses :",student1.courses)                  #
# student2.addCourse("CSE110",4.0,"ENG101",2.7)
# print("student2 Courses :",student2.courses)
# print("########################################\n")
# print(Araf.showStudentInfo(Usis_app,2221010))
# print("########################################\n")
# print(Asif.showStudentInfo(Usis_app,2221022))
# print("########################################\n")
# print(Asif.showStudentInfo(Usis_app,2221011))


# Output
# USIS IS CREATED SUCCESSFULLY !
# hello Araf Sir, welcome to the BRACU!
# hello Araf Sir, Thanks for creating USIS ID
# #######################################

# hello Asif Sir, welcome to the BRACU!
# hello Asif Sir, Thanks for creating USIS ID
# ########################################

# hello Tamim, welcome to the BRACU undergraduate program!
# hello Tamim, Thanks for creating student USIS ID
# ########################################

# hello Kayes, welcome to the BRACU undergraduate program!
# hello Kayes, Thanks for creating student USIS ID
# ########################################

# student1 Courses : {'CSE110': 3.3, 'ENG101': 3.7, 'MAT092': 3.3}
# student2 Courses : {'CSE110': 4.0, 'ENG101': 2.7}
# ########################################

# the student information for id :2221010
# Name: Tamim
# ID: 2221010
# Age: 19
# CGPA: 3.5

# ########################################

# No student with the id: 2221022

# ########################################

# the student information for id :2221011
# Name: Kayes
# ID: 2221011
# Age: 19
# CGPA: 3.25


class Usis:
    def __init__(self, *arg):
        print("USIS IS CREATED SUCCESSFULLY !")
        self.faculty_list = []
        self.student_list = []

    def AddTeacher(self, other):
        self.faculty_list.append(other)
        print(f'hello {other.name} Sir, welcome to the BRACU')
        print(f"hello {other.name} Sir, Thanks for creating USIS ID")

    def AddStudent(self, other):
        self.student_list.append(other)
        print(
            f'hello {other.name}, welcome to the BRACU undergraduate program!')
        print(f"hello {other.name}, Thanks for creating student USIS ID")

    def giveStudentList(self):
        x = self.student_list.copy()  # .copy()--> makes a copy of the list
        return x
