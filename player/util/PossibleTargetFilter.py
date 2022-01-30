from game.Guess import Guess
from lib.words import targetlist


class PossibleTargetFilter:
    def apply(self, history: [Guess]) -> {""}:
        possible_words = targetlist
        for guess in history:
            possible_words = filter(
                lambda word: Guess.evaluate_guess(guess.word, word).matches == guess.matches,
                possible_words
            )
        return possible_words