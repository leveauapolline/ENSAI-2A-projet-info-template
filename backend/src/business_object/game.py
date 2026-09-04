import Player from player
import datetime from datetime


class Game:
    """
        :param player1: The first player.
        :param player2: The second player.
        :param winner: The winning Player, or None if the game is a draw.
        :param game_mode: The type of game played ("coinflip" or "dice").
        :param description: Extra details about the game
        :param timestamp : date
        """

    def __init__(self, player1: Player, player2: Player, game_mode: str, winner: Player, description: str, timestamp: datetime):

        self.id = None  # Will be set once the object is persisted in the database
        self.player1 = player1
        self.player2 = player2
        self.winner = winner
        self.game_mode = game_mode
        self.description = description

    def __str__(self):
        winner_name = self.winner.name if self.winner else "Draw"
        return f"{self.game_mode} between {self.player1.name} and {self.player2.name}. Winner: {winner_name}"
