from business_object.player import Player
from business_object.game import Game
from business_object.game_mode.game_mode import GameMode


class DiceMode(GameMode):
    @staticmethod
    def play(p1: Player, p2: Player, **kwargs) -> Game
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2
 
        description = f"Coin landed on {result}. {p1.name} called {choice}."
 
        return Game(p1, p2, winner, "coinflip", description)


