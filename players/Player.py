from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.provideName()
        self._score = 0

    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def provideName(self):
        raise NotImplementedError

    @abstractmethod
    def getName(self):
        raise NotImplementedError

    @abstractmethod
    def play(self, limit):
        raise NotImplementedError

    # the score is kept the same way throughout all player types
    @property
    def score(self):
        return self._score

    def wins(self):
        print("%s wins!" % (self.getName()))
        self._score += 1

    def reset(self):
        self._score = 0