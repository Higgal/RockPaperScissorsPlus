# import player types
from players.Human import Human
from players.StandardAI import StandardAI
from players.TacticalAI import TacticalAI

# import error / message handling from our helper class
from helpers.ErrorHandler import ErrorHandler

# miscellaneous functions
from helpers.Utility import Utility

from abc import ABC, abstractmethod

class GameMode(ABC):
    # register all opponent player types in the main Mode object
    OpponentTypeRegistry = [
        StandardAI,
        TacticalAI
    ]

    @abstractmethod
    def __init__(self):
        # create the first user (i.e. the player) and prompt for their information
        # then prompt the user for information about player 2. Only two players
        # are supported in a standard Rock Paper Scissors game
        self.player1 = Human()
        print("Great! Player 1 will be called %s" % (self.player1.getName()))

        # prompt the user for the player type and initialize the model on return
        self.player2 = self.selectOpponent()()
        print("Say hello to %s, they will be your opponent." % (self.player2.getName()))        


    # the user will select an opponent from a list of player types specified in the 
    # opponent registry
    def selectOpponent(self):       
        # print out the options
        i = 0
        for mode in self.OpponentTypeRegistry:
            i += 1
            print("[%d] %s" % (i, mode.label))         

        # ask the user to select a valid game mode, or exit
        while True:
            try:
                # print the options + exit
                option = int(input("Please select an opponent: "))
            except ValueError:
                # invalid option type
                ErrorHandler.printColoredMessage("[ERROR]", "Please select a valid option", ErrorHandler.red)
                continue
            except KeyboardInterrupt:
                # user forcefully quits
                ErrorHandler.closeGame()
            else:
                # if the input is beyond the option bounds
                if option < 0 or option > (i):
                    ErrorHandler.printColoredMessage("[ERROR]", "Your choice must be between 0 and %d" % (i), ErrorHandler.red)
                    continue

                # option was valid, break out of loop
                break

        # return the object reference
        return self.OpponentTypeRegistry[option-1]

    def displayScore(self):
        print("%s: %d v.s. %s: %d" % (self.player1.getName(), self.player1.score, self.player2.getName(), self.player2.score))

    # In classic Rock Paper Scissors there are an odd number n of options a player can choose from, where
    # (n-1)/2 number of options are either beaten by you or beat your choice. An elegant way to model and
    # evaluate the result of two options is to create an ordered circular array:
    # 
    # For a given option i1 and i2 where i1 != i2, and a given list of choice n where n is odd, 
    # if i2 belongs to the list: [(i+1) % n, ...,  (i + (n-1)/2) % n] then i1 wins, otherwise, i2 wins
    # because i2 is necessarily "behind" i1 

    # Note: with this system, the classic game's options will be mismatched from the classic chant that usually
    # goes with it... maybe this can be done with models and a win-against relationship, or is that over-engineering?
            
    def takeTurn(self):
        o1 = self.player1.play(self.options)
        o2 = self.player2.play(self.options)

        # if it's a stalemate
        if o1 == o2:
            print("Stalemate!")
            return 0
        else:
            # evaluate the options and declare a winner
            n = len(self.options)
            # the range created here is not the same as the one above, as the function we use requires an exclusive
            # range
            if o2 in Utility.circularRange((o1+1) % n, ((o1 + ((n-1)/2)) + 1) % n, n):
                self.player1.wins()
            else:
                self.player2.wins()

            # we return the largest score for the main game loop. Since scores are incremented by 1, the largest
            # score represents the one closest to possibly crossing the best-of threshold
            if self.player1.score > self.player2.score:
                return self.player1.score
            else:
                return self.player2.score

    def resetScores(self):
        self.player1.reset()
        self.player2.reset()

    @property
    def name(self):
        raise NotImplementedError    

    @property
    def options(self):
        raise NotImplementedError
        
    def getName(self):
        return self.name

    # prints out the options and returns the number of options
    def displayOptions(self):
        i = 0
        for option in self.options:
            # increments start at 1, 0 is exit
            # thus the user's option should be option-1 if it's not 0
            i += 1
            print("[%d] %s" % (i, option))