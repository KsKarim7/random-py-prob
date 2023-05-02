# practice prob 18

class User:
    def __init__(self, name, des, ride='Single'):
        self.name = name
        self.des = des
        self.ride = ride
        self.stat = False
        self.cNum = ''

    def status(self):
        if (self.stat == False):
            print(f"Status: {self.name} is looking for a {self.ride} ride!")
        else:
            print(f"Status: {self.name} boarded in car {self.cNum}!")


class Uber:
    def __init__(self, cNum, ride, *args):
        self.cNum = cNum
        self.ride = ride
        self.lst = []
        for i in args:
            self.lst.append(i)

    def details(self):
        print(f"Car number: {self.cNum} \nType: {self.ride}")
        l = len(self.lst)-1
        print('Routes:', end=' ')
        for i in range(l+1):
            if (self.lst[l] == self.lst[i]):
                print(f'{self.lst[i]}', end=' \n')
            else:
                print(f'{self.lst[i]}', end=' --> ')

    def pick(self, *args):
        for i in args:
            if (i.des in self.lst and i.ride == self.ride):
                print(f'{i.name} has been picked up.')
                i.stat = True
                i.cNum = self.cNum
            elif ((i.des not in self.lst and i.ride != self.ride) or i.ride != self.ride):
                print(f"{i.name} is looking for a different ride.")
            elif (i.ride == self.ride and i.des not in self.lst):
                print(f"{i.name}'s destination is different from this car's route.")


user1 = User("Brooks", "Banani", "Shared")
user2 = User("Jocelyn", "Uttara")
user3 = User("Robert", "Gulshan", "Shared")
user4 = User("Langdon", "Mohakhali", "Shared")


user1.status()
user2.status()
user3.status()
user4.status()
print("----------------------------------")
car1 = Uber("0K32BH", "Shared", "Mohakhali", "Banani", "Nikunja", "Uttara")
car1.details()
print("----------------------------------")
car1.pick(user1, user2, user3, user4)
print("----------------------------------")
user1.status()
user2.status()
user3.status()
user4.status()
print("----------------------------------")
car2 = Uber("5GD2BD", "Single", "Uttara")
car3 = Uber("4T12FR", "Shared", "Gulshan", "Bashundhara")
car2.details()
car3.details()
print("----------------------------------")
car2.pick(user2, user3)
print("----------------------------------")
car3.pick(user3)
print("----------------------------------")
user2.status()
user3.status()
