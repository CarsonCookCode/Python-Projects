

class Game():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class BoardGame(Game):
    def __init__(self, name, numberOfPlayers, forAges):
        self.name = name
        self.numberOfPlayers = numberOfPlayers
        self.forAges = forAges


class VideoGame(Game):
    def __init__(self, name, console, rating):
        self.name = name
        self.console = console
        self.rating = rating







if __name__ == "__main__":

    Halo = VideoGame("Halo", "Xbox", "T")
    print(Halo.name)
    print(Halo.console)
    print(Halo.rating)

    Monopoly = BoardGame("Monopoly", 8, "10 and up")
    print(Monopoly.name)
    print(Monopoly.numberOfPlayers)
    print(Monopoly.forAges)
