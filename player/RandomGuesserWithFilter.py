import random

from game.Game import Game
from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator
from lib.words import targetlist
from player.util.PossibleTargetFilter import PossibleTargetFilter


class RandomGuesserWithFilter(Player):

    def next_guess(self, history: [Guess]) -> str:
        return random.choice(list(PossibleTargetFilter().apply(history)))


if __name__ == '__main__':
    print(PlayerEvaluator.evaluatePlayer(RandomGuesserWithFilter()))
