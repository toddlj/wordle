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

    def test_victory_on_last_guess(self):
        game = Game("hello", SequenceGuesser(["world"]*4 + ["hello"]))
        self.assertTrue(game.victory)


class ConstantGuesser(Player):
    def __init__(self, word):
        self.word = word

    def next_guess(self, history: [Guess]) -> str:
        return self.word


class SequenceGuesser(Player):
    def __init__(self, words: [str]):
        self.words = words
        self.guess_number = 0

    def next_guess(self, history: [Guess]) -> str:
        guess = self.words[self.guess_number]
        self.guess_number += 1
        return guess


if __name__ == '__main__':
    unittest.main()
