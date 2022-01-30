from enum import Enum


class Guess:
    class Match(Enum):
        LETTER_PLACE = 0
        LETTER = 1
        NONE = 2

    def __init__(self, word: str, matches: [Match]):
        self.word = word
        self.matches = matches
