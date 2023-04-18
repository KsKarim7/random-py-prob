# summer 22 final question
# https://drive.google.com/drive/folders/1B3ItZxaUPbovP8L3Cfe-e3feJ_hdTPRR
# question 1
class Monster:
    monsterCount = 3

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.alive = True

    def get_details(self):
        return f'Name: {self.name} \npower: {self.power} \nAlive: {self.alive}'

    def attack(self, *args):
        if (len(args) == 0):
            print('No monsters to attack')
        elif (len(args) == 1):
            if (self.power > args[0].power and self.alive == True):
                print(
                    f'Attack successful. {self.name} defeated {args[0].name}')
                args[0].alive = False
                Monster.monsterCount -= 1
            elif (self.alive != True):
                print(f'{self.name} is not alive to attack')
            else:
                print(
                    f'Attack unsuccessful. {self.name} was defeated by {args[0].name}')
                self.alive = False
                Monster.monsterCount -= 1
        else:
            if (self.power > args[0].power and args[0].alive == True):
                print(
                    f'Attack successful. {self.name} defeated {args[0].name}')
                Monster.monsterCount -= 1
            elif (self.power > args[0].power and args[0].alive == False):
                print(f"Cannot attack {args[0].name}. It's not alive.")
            else:
                print(
                    f'Attack unsuccessful. {self.name} was defeated by {args[0].name}')
                Monster.monsterCount -= 1

            if (self.power > args[1].power and self.alive == True):
                print(
                    f'Attack successful. {self.name} defeated {args[1].name}')
                args[1].alive = False
                Monster.monsterCount -= 1
            elif (self.power > args[1].power and self.alive != True):
                print(f'{self.name} is not alive to attack')
            else:
                print(
                    f'Attack unsuccessful. {self.name} was defeated by {args[1].name}')
                self.alive = False
                Monster.monsterCount -= 1


monster1 = Monster('Godzilla', 40)
monster2 = Monster('Hydra', 30)
monster3 = Monster('KingKong', 50)
print(f"Number of monsters alive:{Monster.monsterCount}")
print('1--------------------------------')
print(monster1.get_details())
print('2--------------------------------')
print(monster2.get_details())
print('3--------------------------------')
print(monster3.get_details())
print('4--------------------------------')
monster1.attack()
print('5--------------------------------')
monster1.attack(monster2)
print('6--------------------------------')
monster1.attack(monster2, monster3)
print('7--------------------------------')
print(f"Number of monsters alive: {Monster.monsterCount}")
print('8--------------------------------')
print(monster2.get_details())
print('9--------------------------------')
monster2.attack(monster1)
