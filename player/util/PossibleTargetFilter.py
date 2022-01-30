from game.Guess import Guess
from lib.words import targetlist


class PossibleTargetFilter:
    def __init__(self):
        self.possible_targets = targetlist

    def apply(self, history: [Guess]) -> {""}:
        self.filter_known_letters_without_counts(history)
        self.filter_guess_outcomes(history)
        return self.possible_targets

    def filter_known_letters_without_counts(self, history):
        known_letters = set()
        for guess in history:
            for i in range(5):
                if guess.matches[i] in {Guess.Match.LETTER_PLACE, Guess.Match.LETTER}:
                    known_letters.add(guess.word[i])
        self.possible_targets = filter(
            lambda word: set(word).issuperset(known_letters),
            self.possible_targets
        )

    def filter_guess_outcomes(self, history):
        for guess in history:
            self.possible_targets = filter(
                lambda word: Guess.evaluate_guess(guess.word, word).matches == guess.matches,
                self.possible_targets
            )
