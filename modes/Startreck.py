from modes.GameMode import GameMode

class Startreck(GameMode):
    name = "Startreck"
    options = [
        'Rock',
        'Scissors',
        'Lizard',
        'Paper',
        'Spock'
    ]

    def __init__(self):
        print("Booting up game in %s mode" % (self.name))
        super().__init__()