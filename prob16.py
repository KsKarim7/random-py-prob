# practice problem 3
class Bird:
    def __init__(self, brb, fly=False):
        self.brb = brb
        self.flyy = fly
        self.type = 'Flightless Birdsj'

    def fly(self):
        if (self.flyy == False):
            print(f'{self.brb} can not fly')
        else:
            print(f'{self.brb} can fly')

    def setType(self, typ):
        self.type = typ

    def printDetail(self):
        print(f'Name: {self.brb} \nType: {self.type}')


ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print('###########################')
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print('=========================')
ostrich.printDetail()
print('=========================')
duck.printDetail()
print('=========================')
owl.printDetail()
