# practice problem 11
# practice problem 11
class Transport:
    total_traveller = 0

    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare
        self.dictt = {}
        self.counter = 0

    def __str__(self):
        s = "Name: "+self.name+", Base fare: "+str(self.baseFare)
        return s


class Bus(Transport):
    def __init__(self, bus, fare):
        super().__init__(bus, fare)
        print(f'Base-fare of {bus} is {fare} Taka')
        self.total_traveller += 3

    def addPassengerWithBags(self, *args):
        count = 1
        for i in range(0, len(args), 2):
            if (args[count] <= 2):
                self.dictt[args[i]] = self.baseFare
            elif (args[count] <= 5):
                self.dictt[args[i]] = self.baseFare + 60
            else:
                self.dictt[args[i]] = self.baseFare + 105
            count += 2
            self.counter += 1
            Transport.total_traveller += 1

    def __str__(self):
        s = super().__str__() + "\nTotal Passenger(s): " + \
            str(self.counter) + "\nPassenger details:"
        for k, v in self.dictt.items():
            s += f'\nName: {k}, Fare: {v}'
        return s


class Train(Transport):
    def __init__(self, bus, fare):
        super().__init__(bus, fare)
        print(f'Base-fare of {bus} is {fare} Taka')
        countt = 5

    def addPassengerWithBags(self, *args):
        count = 1
        for i in range(0, len(args), 2):
            if (args[count] <= 2):
                self.dictt[args[i]] = self.baseFare
            elif (args[count] <= 5):
                self.dictt[args[i]] = self.baseFare + 60
            else:
                self.dictt[args[i]] = self.baseFare + 105
            count += 2
            self.counter += 1
            Transport.total_traveller += 1

    def __str__(self):
        s = super().__str__() + "\nTotal Passenger(s): " + \
            str(self.counter) + "\nPassenger details:"
        for k, v in self.dictt.items():
            s += f'\nName: {k}, Fare: {v}'
        return s


t1 = Bus("Volvo", 950)
print("=================================")
t1.addPassengerWithBags("David", 6,  "Mike", 1, "Carol", 3)
print("=================================")
print(t1)
print("=================================")
t2 = Train("Silk City", 850)
print("=================================")
t2.addPassengerWithBags("Bob", 2, "Simon", 4)
print("=================================")
print(t2)
print("=================================")
print("Total Passengers in Transport: ", Transport.total_traveller)
