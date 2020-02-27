# import game modes and then register in the ModeRegistry list array
from modes.Classic import Classic
from modes.Startreck import Startreck

# import error / message handling from our helper class
from helpers.ErrorHandler import ErrorHandler

# misc functions
from helpers.Utility import Utility

class Game:
    'Main Game Object'

    # register all modes in the main Game object
    ModeRegistry = [
        Classic,
        Startreck
    ]

    def __init__(self):
        # first run the initialization procedure then begin the game loop, 
        # after which it'll prompt the user to either exit or start a new game        
        print("Welcome to Rock Paper Scissors!")
        print("Select a Game Mode You Want to Play:")

        # get the initiator to select a game mode
        self.mode = self.provideMode()()

        input("Press enter to continue")

        # game repeat loop starts here
        while True:
            # clear output for cleanliness
            Utility.clearScreen()     

            # reset the scores
            self.mode.resetScores()

            # standard rock-paper-scissors games go on until the best-of-n rule is satisfied
            # n must be odd and equal or larger than 0. We will pre-empt users wanting only
            # one game

            while True:
                try:
                    numGames = int(input("Best of: "))
                except ValueError:
                    # invalid option type
                    ErrorHandler.printColoredMessage("[ERROR]", "Number of matches must be an odd integer.", ErrorHandler.red)
                    continue                
                except KeyboardInterrupt:
                    # user forcefully quits
                    ErrorHandler.closeGame()            
                else:
                    # matches must be positive odd number
                    if numGames < 0 or numGames % 2 == 0:
                        ErrorHandler.printColoredMessage("[ERROR]", "Number of matches must be an odd integer.", ErrorHandler.red)
                        continue
                    
                    break

            # mode and players are created, begin the main play loop
            # largest score is incremented by one before being halved to avoid having to import math to ceil
            largestScore = 0
            while largestScore < (numGames+1)/2:
                # print out the options from the game mode
                self.mode.displayOptions()
                
                # use the mode object to dictate the round
                # the mode object evaluates the results of the roun, and only positive results
                # can increment the play count (as stalemates don't count towards the best-of-n counter)
                largestScore = self.mode.takeTurn()

            # print out the score
            self.mode.displayScore()

            while True:
                try:
                    option = input("Play again? [y/n]: ")
                except KeyboardInterrupt:
                    # user forcefully quits
                    ErrorHandler.closeGame() 
                else:
                    if option.lower() == 'y':
                        # game continues another loop
                        break
                    elif option.lower() == 'n':
                        ErrorHandler.closeGame()
                    else:
                        ErrorHandler.printColoredMessage("[ERROR]", "Please select a valid option", ErrorHandler.red)
                        continue

            # one more go
            continue


    def provideMode(self):
        # user can exit at any time during the initialization procedure
        # add the exit option
        print("[%d] %s" % (0, "Exit"))
        
        # print out the options
        i = 0
        for mode in self.ModeRegistry:
            i += 1
            print("[%d] %s" % (i, mode.name))
            

        # ask the user to select a valid game mode, or exit
        while True:
            try:
                # print the options + exit
                option = int(input("Please select a game mode: "))
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

                if option == 0:
                    ErrorHandler.closeGame()

                # option was valid, break out of loop
                break

        return self.ModeRegistry[option-1]