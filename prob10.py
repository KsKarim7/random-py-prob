# CSE111 Fall-22(final question)
# https://drive.google.com/file/d/1CP9qKbmYsX_557R-k6zX1y8Ryf6ueuHU/view?usp=share_link

# question 01

class Netflix:
    shows_no = 0
    shows = []

    def __init__(self, show, genre, ep=10):
        self.show = show
        self.genre = ', '.join(genre)
        self.ep = ep
        Netflix.shows_no += 1
        Netflix.shows.append(self.show)

    def __str__(self):
        return f'Show name: {self.show} \nEpisodes: {self.ep} \nGenre: {self.genre}'

    @staticmethod
    def printDetails():
        print(f"Total number of shows: {Netflix.shows_no}")
        for i in Netflix.shows:
            print(i)


s1 = Netflix("Wednesday", ["Mystery", "Supernatural"], 15)
print("==========1==========")
print(s1)
s2 = Netflix("Dark", ["Mind-Bending", "Sci-fi"])
print("==========2==========")
print(s2)
print("==========3==========")
Netflix.printDetails()
s3 = Netflix("Suits", ["Comedy", "Courtroom"], 20)
print("==========4==========")
print(s3)
s4 = Netflix("Demon Slayer", ["Anime"], 22)
print("==========5==========")
print(s4)
print("==========6==========")
Netflix.printDetails()
