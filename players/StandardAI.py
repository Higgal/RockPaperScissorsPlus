from players.Player import Player
import random
import re

# import error / message handling from our helper class
from helpers.ErrorHandler import ErrorHandler
from helpers.Utility import Utility

class StandardAI(Player):
    # static component to class object
    label = "Standard CPU"

    @property
    def name(self):
        return self._name

    # AIs obtain their names from a randomized selector in a helper method
    def provideName(self):
        self._name = Utility.getRandomName()

    # get the player name
    def getName(self):
        return self._name

    # standard AI choose a random option
    def play(self, options):
        # choose a random number between [1, n+1[ thus an exclusive n+1 
        # is inclusive n, where n is the number of options
        i = random.randrange(1, len(options)+1)-1
        print("%s chooses %s" % (self._name, options[i]))
        return i