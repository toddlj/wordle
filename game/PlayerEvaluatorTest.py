import unittest

from game.Guess import Guess
from game.Player import Player
from game.PlayerEvaluator import PlayerEvaluator
from lib.words import targetlist


class PlayerEvaluatorTest(unittest.TestCase):
    def test_evaluator(self):
        evaluator = PlayerEvaluator(ConstantGuesser("hello"))
        evaluator.evaluate()

        self.assertEqual(evaluator.victories, ["hello"])
        self.assertNotIn("hello", evaluator.losses)
        self.assertEqual(len(evaluator.losses), len(targetlist) - 1)


class ConstantGuesser(Player):
    def __init__(self, word):
        self.word = word

    def next_guess(self, history: [Guess]) -> str:
        return self.word


if __name__ == '__main__':
    unittest.main()
