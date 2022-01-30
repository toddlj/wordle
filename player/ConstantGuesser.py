from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator


class ConstantGuesser(Player):
    def __init__(self):
        self.word = "hello"

    def next_guess(self, history: [Guess]) -> str:
        return self.word


if __name__ == '__main__':
    print(PlayerEvaluator.evaluate_player(ConstantGuesser))
