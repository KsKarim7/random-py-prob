# Practice prob 2
class myList:
    count = 0

    def __init__(self, *args):
        self.sum = 0
        self.args = args
        # print(self.lst)
        for i in args:
            self.sum += i
            myList.count += 1
        # print(self.sum, myList.count)

    def summ(self):
        # for i in self.args:
        print(f'Sum: {self.sum}')

    def merge(self, *args):
        for i in args:
            self.sum += i
            myList.count += 1

    def average(self):
        if (self.sum == 0):
            print(f'Average: 0')
        else:
            print(f'Average: {(self.sum/myList.count)}')


# you might need a list inside your class to store the values
l1 = myList(2, 3, 4, 5, 6)
l1.summ()
l1.merge(4, 5, 9)
l1.summ()
l1.average()
print("-----------------------------")
l2 = myList()
l2.average()
l2.merge(1, 2, 4, 8)
l2.summ()
