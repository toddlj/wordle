import random
import timeit

from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator
from player.util.PossibleTargetFilter import PossibleTargetFilter


class RandomGuesserWithFilter(Player):

    def next_guess(self, history: [Guess]) -> str:
        return random.choice(list(PossibleTargetFilter().apply(history)))


if __name__ == '__main__':
    start_time = timeit.default_timer()
    print(PlayerEvaluator.evaluate_player(RandomGuesserWithFilter))
    print(f"In {timeit.default_timer() - start_time} seconds")
