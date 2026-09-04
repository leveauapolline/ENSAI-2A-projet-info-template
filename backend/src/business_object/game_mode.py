from abc import abstractmethod

from business_object.game import Game
from business_object.player import Player


class GameMode(abstractmethod):
    """Abstract base class for all game modes (coinflip, dice, ...)."""

    @abstractmethod
    def play(self, p1: Player, p2: Player, **kwargs) -> Game:
        """
        Play one game between p1 and p2 following this mode's rules.

        :param p1: The first player.
        :param p2: The second player.
        :param kwargs: Extra parameters specific to the mode (for example the choice for coinflip).
        :return: The resulting Game object.
        """
        pass
