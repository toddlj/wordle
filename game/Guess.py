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
        if target not in targetlist:
            raise Exception("target not in target list")
        if guess not in guesslist:
            raise Exception("guess not in guess list")

        matches = [Guess.Match.NONE]*5

        letter_place_match_indices = []
        for i in range(0, 5):
            if target[i] == guess[i]:
                matches[i] = Guess.Match.LETTER_PLACE
                letter_place_match_indices += [i]

        unmatched_indices = list(set(range(0, 5)).difference(letter_place_match_indices))
        for letter in set(guess):
            guess_partial_matches = list(filter(lambda i: guess[i] == letter, unmatched_indices))
            target_partial_matches = list(filter(lambda i: target[i] == letter, unmatched_indices))
            partial_match_count = min(len(guess_partial_matches), len(target_partial_matches))

            for i in guess_partial_matches[:partial_match_count]:
                matches[i] = Guess.Match.LETTER

        return Guess(guess, matches)
