class Library:
    Total_book = 1000
    borrow_data = {}

    def __init__(self, n, id):
        self.student_name = n
        self.student_id = id

    def borrowbook(self):
        print("A book is borrowed!")

    def __str__(self):
        return "Library: XYZ"

# Write your code here


class Student(Library):
    lst = []

    def __init__(self, name, id):
        super().__init__(name, id)
        self.library = "XYZ"
        # self.dict = {}

    def borrowbook(self, book, uId=None):
        self.book = book
        self.uId = uId
        if (book in Student.lst):
            print(
                f"Sorry {self.student_name} ! {book} is borrowed by {str(Library.borrow_data[book])[1:-1]}")
        else:
            if (book not in Library.borrow_data):
                Library.borrow_data[book] = [self.student_name]
            else:
                Library.borrow_data[book] += self.student_name
            print(f'A book is borrowed')
            Library.Total_book -= 1
            Student.lst.append(book)
            if (uId == None):
                print(f"'{self.book}' book is borrowed by {self.student_name}({self.student_id}) \nNumber of books available for borrowing = {Library.Total_book}")
            else:
                print(f"'{self.book}' book with unique id {self.uId} is borrowed by {self.student_name}({self.student_id}) \nNumber of books available for borrowing = {Library.Total_book}")

    def __str__(self):
        return f"Library: {self.library} \nStudent Name: {self.student_name} ID: {self.student_id} \nBooks borrowed: {str(Student.lst)[1:-1]}"

    def returnAllBooks(self):
        for k, v in Library.borrow_data.items():
            # if (v[1:-1] == self.student_name):
            #     Library.borrow_data.pop(k)
            # if (str(v)[1:-1] == self.student_name):
            #     print(k, v)
            # else:
            #     print('payna')
            for i in v:
                if (i == self.student_name):
                    # Library.borrow_data.pop(k)
                    del Library.borrow_data[k]
                else:
                    print('pyna')


s1 = Student("Alice", 18101259)
s1.borrowbook("The Alchemist", "Hdw652")
print("===============")
print(s1)
print("===============")
print(Library.borrow_data)
print("===============")
s1.borrowbook("Wuthering Heights")
print("===============")
print(s1)
print("===============")
s2 = Student("David", 18141777)
s2.borrowbook("The Alchemist", "Hdw652")
print("===============")
s2.borrowbook("The Vampyre")
print("===============")
print(Library.borrow_data)
print("===============")
s1.returnAllBooks()
print("===============")
print(Library.borrow_data)
