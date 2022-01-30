from game.Game import Game
from game.Player import Player
from lib.words import targetlist


class PlayerEvaluator:
    def __init__(self, player: Player):
        self.player = player
        self.losses = []
        self.victories = []
        self.evaluated = False

    def evaluate(self):
        for target in targetlist:
            if Game(target, self.player).victory:
                self.victories += [target]
            else:
                self.losses += [target]
        self.evaluated = True

    def results(self) -> str:
        if not self.evaluated:
            raise Exception("Results not ready")
        return f"Victories={len(self.victories)}, Losses={len(self.losses)}, Percentage won: {len(self.victories) / (len(self.losses) + len(self.victories)) * 100} %"
