from game.Guess import Guess
from game.Player import Player


class Game:
    def __init__(self, target: str, player: Player):
        self.target = target
        self.player = player
        self.history = self.run_game()
        self.victory = Guess.FULL_MATCH in list(map(lambda guess: guess.matches, self.history))

    def run_game(self, rounds=5) -> [Guess]:
        history = []
        for _ in range(rounds):
            history += [Guess.evaluate_guess(self.player.next_guess(history), self.target)]
        return history

