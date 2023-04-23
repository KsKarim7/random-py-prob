# Practice Problem 1
class PlayerEarning:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.bonus = 0
        self.earning = 0

    def calculateTotal(self, earnings, goal=0):
        if (goal == 0):
            self.bonus = 0
            self.total = earnings
            self.earning = earnings
        elif (goal > 30):
            self.bonus = int((5/100) * earnings + 10000)
            self.total += earnings + self.bonus
            self.earning = earnings
        else:
            self.bonus = int((5/100) * earnings)
            self.total += earnings + self.bonus
            self.earning = earnings

    def printDetails(self):
        print(f'Player name: {self.name} \nPlayer Season Earning without bonus: {self.earning} \nBonus: {self.bonus} \nPlayer Season Earning After Bonus: {self.total}')


print("**********************")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()

print("\n**********************")
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000, 31)
player2.printDetails()

print("\n**********************")
player3 = PlayerEarning('Cuadrado')
player3.calculateTotal(250000, 20)
player3.printDetails()
