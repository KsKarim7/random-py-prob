# Question : https://drive.google.com/file/d/1X8l7V2TZfaA-atO7xLoyua-YH1C8Kd1_/view?usp=sharing

class Anime:
    def __init__(self, title, arg=None):
        self.title = title
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
        print(
            f'Title: {self.title} \nYear: {self.year} \nSeason: {self.season}')


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
