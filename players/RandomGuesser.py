import random

from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator
from lib.words import targetlist


class RandomGuesser(Player):

    def next_guess(self, history: [Guess]) -> str:
        return random.choice(list(targetlist))


if __name__ == '__main__':
    print(PlayerEvaluator.evaluatePlayer(RandomGuesser()))
