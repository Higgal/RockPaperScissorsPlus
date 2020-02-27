from players.Player import Player
import re

# import error / message handling from our helper class
from helpers.ErrorHandler import ErrorHandler

class Human(Player):
    # static component to class object
    label = "Human"

    @property
    def name(self):
        return self._name

    # human players are given a name from user input
    def provideName(self):
        while True:
            # get the name from input.
            # TODO: trim spaces from string for better UX 
            userInput = input("What's your name: ")

            # user input must be a valid char-only string
            # composed of only english alphabet
            if not re.match("^[a-zA-Z]*$", userInput):
                ErrorHandler.printColoredMessage("[ERROR]", "Name must be only alphabetical characters", ErrorHandler.red)
            else:
                # name was valid, break out of loop
                break

        self._name = userInput

    # humans get prompted for their option
    # play receivs a limit which represents the last index of the
    # current mode's option 
    def play(self, options):
        # ask the user to input a choice, the list of options is provided in the mode layer
        while True:
            try:
                # print the options + exit
                option = int(input(self._name + ", you play: "))
            except ValueError:
                # invalid option type
                ErrorHandler.printColoredMessage("[ERROR]", "Please select a valid option", ErrorHandler.red)
                continue
            except KeyboardInterrupt:
                # user forcefully quits
                ErrorHandler.closeGame()            
            else:
                # if the input is beyond the option bounds
                if option < 1 or option > (len(options)):
                    ErrorHandler.printColoredMessage("[ERROR]", "Your choice must be between 0 and %d" % (len(options)), ErrorHandler.red)
                    continue

                # option was valid, break out of loop
                break

        # correct the choice to better represent a subscript in a list
        return option-1

    # get the player name
    def getName(self):
        return self._name

    