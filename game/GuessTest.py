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

    def testEvaluatesLettersInWrongPlaceWithMultipleRepeats(self):
        guess = "hello"
        target = "world"
        matches = [Guess.Match.NONE,
                   Guess.Match.NONE,
                   Guess.Match.LETTER,
                   Guess.Match.NONE,
                   Guess.Match.LETTER]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)

    def testEvaluatesLettersInWrongPlace(self):
        guess = "world"
        target = "hello"
        matches = [Guess.Match.NONE,
                   Guess.Match.LETTER,
                   Guess.Match.NONE,
                   Guess.Match.LETTER,
                   Guess.Match.NONE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)

    def testEvaluatesLettersInWrongPlaceWithSomeFullMatches(self):
        guess = "bowls"
        target = "world"
        matches = [Guess.Match.NONE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.LETTER,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.NONE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)

    def testEvaluatesTwoLettersInWrongPlace(self):
        guess = "boots"
        target = "taboo"
        matches = [Guess.Match.LETTER,
                   Guess.Match.LETTER,
                   Guess.Match.LETTER,
                   Guess.Match.LETTER,
                   Guess.Match.NONE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)

    def testEvaluatesLettersInWrongPlaceAndFullMatchForSameLetter(self):
        guess = "maims"
        target = "gamma"
        matches = [Guess.Match.LETTER,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.NONE,
                   Guess.Match.LETTER_PLACE,
                   Guess.Match.NONE]

        self.assertEqual(Guess.evaluate_guess(guess, target).matches, matches)


if __name__ == '__main__':
    unittest.main()
