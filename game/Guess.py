from enum import Enum

from lib.words import targetlist, guesslist


class Guess:
    class Match(Enum):
        LETTER_PLACE = 0
        LETTER = 1
        NONE = 2

    def __init__(self, word: str, matches: [Match]):
        self.word = word
        self.matches = matches

    @staticmethod
    def evaluate_guess(guess: str, target: str):
        if (target not in targetlist):
            raise Exception("target not in target list")
        if (guess not in guesslist and guess not in targetlist):
            raise Exception("guess not in guess list")

        matches = [Guess.Match.NONE]*5

        return Guess(guess, matches)
