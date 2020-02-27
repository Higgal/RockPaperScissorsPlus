# colors for UX
from termcolor import colored
import colorama
import sys

colorama.init()

class ErrorHandler:
    "Centralizes the Error Printing"

    # colors for UX
    # colors work for Mac and Windows TODO: test Linux and other OSs
    yellow = "yellow"
    red = "red"
    green = "green"
    blue = "blue"

    def __init__(self):
        pass

    @staticmethod
    def printColoredMessage(status, message, color):
        print(colored(status, color), message)
        pass

    # exits the game in a graceful way
    # TODO can the exit script do some garbage collection or optimization?
    @staticmethod
    def closeGame():
        print("Goodbye!")
        sys.exit()