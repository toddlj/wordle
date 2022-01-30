from collections import Counter

from game.Guess import Guess
from lib.words import targetlist


class PossibleTargetFilter:
    def __init__(self):
        self.possible_targets: {""} = targetlist

    def apply(self, history: [Guess]) -> None:
        self.filter_known_letters_without_counts(history)
        self.filter_known_letter_places(history)
        self.filter_guess_outcomes(history)

    def filter_known_letters_without_counts(self, history: [Guess]):
        known_letters = set()
        for guess in history:
            for i in range(5):
                if guess.matches[i] in {Guess.Match.LETTER_PLACE, Guess.Match.LETTER}:
                    known_letters.add(guess.word[i])
        self.possible_targets = set(filter(
            lambda word: set(word).issuperset(known_letters),
            self.possible_targets
        ))

    def filter_known_letter_places(self, history: [Guess]):
        known_letter_places = {}
        for guess in history:
            for i in range(5):
                if guess.matches[i] == Guess.Match.LETTER_PLACE:
                    known_letter_places[i] = guess.word[i]

        for position in known_letter_places.keys():
            self.possible_targets = set(filter(
                lambda word: word[position] == known_letter_places[position],
                self.possible_targets
            ))

    def filter_guess_outcomes(self, history):
        for guess in history:
            self.possible_targets = set(filter(
                lambda word: Guess.evaluate_guess(guess.word, word).matches == guess.matches,
                self.possible_targets
            ))
