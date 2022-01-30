from typing import Callable

from game.Game import Game
from game.Player import Player
from lib.words import targetlist


class PlayerEvaluator:
    def __init__(self, player_constructor: Callable[[], Player]):
        self.player_constructor = player_constructor
        self.losses = []
        self.victories = []
        self.evaluated = False

    def evaluate(self):
        for target in targetlist:
            if Game(target, self.player_constructor()).victory:
                self.victories += [target]
            else:
                self.losses += [target]
        self.evaluated = True

    def results(self) -> str:
        if not self.evaluated:
            raise Exception("Results not ready")
        return f"Victories={len(self.victories)}, Losses={len(self.losses)}, Percentage won: {len(self.victories) / (len(self.losses) + len(self.victories)) * 100} %"

    @staticmethod
    def evaluate_player(player_constructor: Callable[[], Player]) -> str:
        evaluator = PlayerEvaluator(player_constructor)
        evaluator.evaluate()
        return evaluator.results()
