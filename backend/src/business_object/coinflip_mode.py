import secrets

from business_object.game_mode.game_mode import GameMode

from business_object.game import Game
from business_object.player import Player


class CoinFlipMode(GameMode):
    """Game mode where a coin is flipped: the player who guessed right wins."""
    @staticmethod
    def play(p1: Player, p2: Player, choice: str = "heads", **kwargs) -> Game:
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        description = f"Coin landed on {result}. {p1.name} called {choice}."

        return Game(p1, p2, winner, "coinflip", description)
