# practice prob 15
class Player:
    database = {}
    playerNo = 0

    def __init__(self, name, team, jerseyNo):
        self.name = name
        self.team = team
        self.jerseyNo = jerseyNo

    def __str__(self):
        return "Name:{}\nTeam:{}\nJersey No:{}".format(self.name, self.team, self.jerseyNo)

# Write your code here


class FootballPlayer(Player):

    def __init__(self, *args):
        super().__init__(args[0], args[1], args[2])
        self.goals = str(args[3])
        if (len(args) == 5):
            self.rDate = args[4]
        else:
            self.rDate = None
        Player.playerNo += 1
        first, second = self.name.split(' ')
        self.id = str(Player.playerNo) + \
            first[0] + second[0] + str(self.jerseyNo)
        for i in args:
            if (self.id in Player.database):
                Player.database[self.id] += [i]
            else:
                Player.database[self.id] = [i]

    def __str__(self):
        if (self.rDate == None):
            return f"Player ID: {self.id} \nName: {self.name} \nTeam: {self.team} \nJeysey No: {self.jerseyNo} \nGoals Scored: {self.goals} \nRetirement date: Not yet retired"
        else:
            return f"Player ID: {self.id} \nName: {self.name} \nTeam: {self.team} \nJeysey No: {self.jerseyNo} \nGoals Scored: {self.goals} \nRetirement date: {self.rDate}"

    @classmethod
    def createPlayer(cls, name, team, jno, goals, rData):
        obj = cls(name, team, jno, goals, rData)
        return obj


print("Number of players:", Player.playerNo)
print("Player Database:", Player.database)
print("#################################")
p1 = FootballPlayer("Lionel Messi", "Barcelona", 10, 231)
print("------Details of the player------")
print(p1)
print("#################################")
p2 = FootballPlayer("Cristiano Ronaldo", "Juventus", 7, 215)
print("------Details of the player------")
print(p2)
print("#################################")
p3 = FootballPlayer.createPlayer(
    "Miroslav Klose", "Lazio", 11, 71, "11 Aug,2014")
print("------Details of the player------")
print(p3)
print("#################################")
print("Number of players:", Player.playerNo)
print("Player Database:", Player.database)
