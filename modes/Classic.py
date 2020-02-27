from modes.GameMode import GameMode

class Classic(GameMode):
    name = "Classic"
    options = [
        'Rock',
        'Scissors',
        'Paper'
    ]

    def __init__(self):
        print("Booting up game in %s mode" % (self.name))
        super().__init__()