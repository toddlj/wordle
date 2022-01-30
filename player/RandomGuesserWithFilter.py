import random

from game.Game import Game
from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator
from lib.words import targetlist


class RandomGuesserWithFilter(Player):

    def next_guess(self, history: [Guess]) -> str:
        possible_words = targetlist
        for guess in history:
            possible_words = filter(
                lambda word: Guess.evaluate_guess(guess.word, word).matches == guess.matches,
                possible_words
            )
        return random.choice(list(possible_words))


if __name__ == '__main__':
    print(PlayerEvaluator.evaluatePlayer(RandomGuesserWithFilter()))
