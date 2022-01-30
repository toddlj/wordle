import unittest

from game.Game import Game
from game.Guess import Guess
from game.Player import Player


class GameTest(unittest.TestCase):
    def test_victory(self):
        game = Game("hello", ConstantGuesser("hello"))
        self.assertTrue(game.victory)

    def test_loss(self):
        game = Game("hello", ConstantGuesser("world"))
        self.assertFalse(game.victory)


class ConstantGuesser(Player):
    def __init__(self, word):
        self.word = word

    def next_guess(self, history: [Guess]) -> str:
        return self.word


if __name__ == '__main__':
    unittest.main()
