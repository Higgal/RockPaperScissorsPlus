from os import system, name
import random

class Utility:
    "Miscellaneous Functions"

    # retrieves a list of integers in a circular format
    @staticmethod
    def circularRange(start, stop, modulo):
        result = []
        i = start

        while i != stop:
            result.append(i)
            i = (i + 1) % modulo
        return result

    # define our clear function 
    @staticmethod
    def clearScreen(): 
    
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    @staticmethod
    def getRandomName():
        nameList = [
            'Alice',
            'Bob',
            'Charlie',
            'Decard',
            'Edward',
            'Felix',
            'George',
            'Haris',
            'Ian',
            'John',
            'Kendrick',
            'Lloyd',
            'Margot',
            'Nancy',
            'Ophelia',
            'Penelope',
            'Quinn',
            'Rupert',
            'Stan',
            'Trevor',
            'Usain',
            'Victor',
            'William',
            'Xavier',
            'Yuri',
            'Zachary'
        ]        

        return random.choice(nameList)