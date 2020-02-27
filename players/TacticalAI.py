from players.Player import Player
import random
import re

# import error / message handling from our helper class
from helpers.ErrorHandler import ErrorHandler
from helpers.Utility import Utility

class TacticalAI(Player):
    # static component to class object
    label = "Tactical CPU"

    def __init__(self):
        super().__init__()

        # initialize the AI with having chosen no previous option
        self.lastOption = None

    @property
    def name(self):
        return self._name

    # AIs obtain their names from a randomized selector in a helper method
    def provideName(self):
        self._name = Utility.getRandomName()

    # get the player name
    def getName(self):
        return self._name

    # tactical AI chooses an option that beats its previous one
    def play(self, options):
        # current behavior is to first randomly choose an option, then proceed
        # with the beat-last-option tactic. This behavior can always change

        if self.lastOption is None:
            # choose a random number between [1, n+1[ thus an exclusive n+1 
            # is inclusive n, where n is the number of options
            i = random.randrange(1, len(options)+1)-1
        else:
            # last option is set, choose the option that will beat it (i.e. the index
            # counter-clockwise to the last option)

            # TODO: the CPU selects the FIRST option that beats its choice. In game modes that 
            # have options that are beaten by more than 1 choice, we can implement randomness
            # in the mix:
            # e.g. if the last option was "Rock", the CPU will randomly select either "Paper" or "Spock"
            
            i = (self.lastOption - 1) % len(options)

        self.lastOption = i
        print("%s chooses %s" % (self._name, options[i]))
        return i