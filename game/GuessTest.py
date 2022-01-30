import unittest

from game.Guess import Guess


class GuessTest(unittest.TestCase):
    def testEvaluatesNoMatch(self):
        guess = "gains"
        target = "hello"
        matches = [Guess.Match.NONE,
                   Guess.Match.NONE,
                   Guess.Match.NONE,
                   Guess.Match.NONE,
                   Guess.Match.NONE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)

    def testEvaluatesFullMatch(self):
        guess = "hello"
        target = "hello"
        matches = [Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER_PLACE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)

    def testEvaluatesPartialFullMatch(self):
        guess = "helps"
        target = "hello"
        matches = [Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.NONE,
                   Guess.Match.NONE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)


if __name__ == '__main__':
    unittest.main()
