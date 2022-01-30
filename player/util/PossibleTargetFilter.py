from game.Guess import Guess
from lib.words import targetlist


class PossibleTargetFilter:
    def apply(self, history: [Guess]) -> {""}:
        possible_targets = targetlist
        for guess in history:
            possible_targets = filter(
                lambda word: Guess.evaluate_guess(guess.word, word).matches == guess.matches,
                possible_targets
            )
        return possible_targets
