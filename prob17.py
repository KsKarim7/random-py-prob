# practice problem 4
class Account:
    count = 0

    def __init__(self, name, age, prof, amount):
        self.name = name
        self.age = age
        self.prof = prof
        self.amount = amount
        Account.count += 1

    def addMoney(self, amount):
        self.amount += amount

    def withdrawMoney(self, amount):
        if (self.amount < amount):
            pass
        else:
            self.amount -= amount

    def printDetails(self):
        print(
            f'Name: {self.name} \nAge: {self.age} \nOccupation: {self.prof} \nTotal Amount: {self.amount}')


print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================")
print('No of account holders:', Account.count)
