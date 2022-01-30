from game.Guess import Guess
from lib.words import targetlist


class PossibleTargetFilter:
    def __init__(self):
        self.possible_targets: {""} = targetlist

    def apply(self, history: [Guess]) -> None:
        new_word = history[-1] if len(history) > 0 else None

        if new_word:
            self.filter_known_letters_without_counts(new_word)
            self.filter_known_letter_places(new_word)
            self.filter_guess_outcomes(new_word)

    def filter_known_letters_without_counts(self, guess: Guess):
        known_letters = set()
        for i in range(5):
            if guess.matches[i] in {Guess.Match.LETTER_PLACE, Guess.Match.LETTER}:
                known_letters.add(guess.word[i])
        self.possible_targets = set(filter(
            lambda word: set(word).issuperset(known_letters),
            self.possible_targets
        ))

    def filter_known_letter_places(self, guess: Guess):
        known_letter_places = {}
        for i in range(5):
            if guess.matches[i] == Guess.Match.LETTER_PLACE:
                known_letter_places[i] = guess.word[i]

        for position in known_letter_places.keys():
            self.possible_targets = set(filter(
                lambda word: word[position] == known_letter_places[position],
                self.possible_targets
            ))

    def filter_guess_outcomes(self, guess: Guess):
        self.possible_targets = set(filter(
            lambda word: Guess.evaluate_guess(guess.word, word).matches == guess.matches,
            self.possible_targets
        ))
