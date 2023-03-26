# Question : https://drive.google.com/file/d/1X8l7V2TZfaA-atO7xLoyua-YH1C8Kd1_/view?usp=sharing

class Anime:
    def __init__(self, title, arg=None):
        self.title = title
        self.total_budget = 0
        self.chr = {}
        if (arg == None):
            self.year = 2023
            self.season = 'Spring'
        else:
            # if ('#' in arg):
            #     self.year, self.season = arg.split('#')
            # else:
            if (type(arg) is int):
                self.year = arg
                self.season = 'Spring'
            else:
                if ('#' in arg):
                    self.season, self.year = arg.split('#')
                else:
                    self.year = 2023
                    self.season = arg

    def animeInfo(self):
        if (self.total_budget == 0):
            print(
                f'Title: {self.title} \nYear: {self.year} \nSeason: {self.season}')
        else:
            print(
                f'Title: {self.title} \nYear: {self.year} \nSeason: {self.season} \nTotal Budget: {self.total_budget} \nCharacters: {self.chr}')

    def buildCharacter(self, *args):
        cost = {'Male': 400, 'Female': 500,
                'Protag': 200, 'Antag': 170, 'Mob': 100}
        self.count = len(args) // 2
        sum = 0
        print(f'{self.count} characters added to {self.title}')
        for i in range(0, len(args), 2):
            for j in args[i + 1]:
                sum += cost[j]
            if (len(args[i+1]) == 1):
                sum += cost['Mob']
            self.chr[args[i]] = sum
            self.total_budget += sum
            sum = 0

    def compareBudget(self, obj):
        if (self.total_budget > obj.total_budget):
            return f'{self.title} has more budget than {obj.title}'
        elif (self.total_budget < obj.total_budget):
            return f'{self.title} has less budget than {obj.title}'
        else:
            return f'{self.title} and {obj.title} has equal budget'


a1 = Anime('Oshi No Ko')
a2 = Anime('Kakushigoto', 2020)
a3 = Anime('Tomo Chan', 'Winter')
a4 = Anime('Vanitas', 'Summer#2021')
print('1#####################')
a1.animeInfo()
print('2#####################')
a2.animeInfo()
print('3#####################')
a3.animeInfo()
print('4#####################')
a4.animeInfo()
print('5#####################')
a1.buildCharacter('Hoshino', ['Female',
                              'Protag'], 'Gorou', ['Male', 'Antag'],
                  'Pieyon', ['Male'])
print('---------------------')
a1.animeInfo()
print('6#####################')
a2.buildCharacter('Kakushi', ['Male',
                              'Protag'], 'Hime', ['Female',
                                                  'Protag'])
print('---------------------')
a2.animeInfo()
print('7#####################')
a3.buildCharacter('Ferris', ['Female'])
print('---------------------')
a3.animeInfo()
print('8#####################')
a4.buildCharacter('Noe', ['Male', 'Protag'])
print(f'Total Budget of {a4.title} is {a4.total_budget}')
print('9#####################')
print(a1.compareBudget(a2))
print(a3.compareBudget(a2))
print(a3.compareBudget(a4))
