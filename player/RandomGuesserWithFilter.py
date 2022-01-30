import random
import timeit

from game.Game import Game
from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator
from player.util.PossibleTargetFilter import PossibleTargetFilter


class RandomGuesserWithFilter(Player):

    def __init__(self):
        self.possible_target_filter = PossibleTargetFilter()

    def next_guess(self, history: [Guess]) -> str:
        self.possible_target_filter.apply(history)
        return random.choice(list(self.possible_target_filter.possible_targets))


if __name__ == '__main__':
    start_time = timeit.default_timer()
    print(PlayerEvaluator.evaluate_player(RandomGuesserWithFilter))
    print(f"In {timeit.default_timer() - start_time} seconds")
