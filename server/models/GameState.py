#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

import os
from models.Player import Player
from redis import Redis

class GameState:
    def __init__(self):
        self._redis = Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"))

        player_names = [str(key).split(":")[1] for key in self._redis.keys("PLAYER:*")]
        self._players: list[Player] = [
            Player(name, self._redis) for name in player_names
        ]

    # region ----- admin -----
    
    def get_player_scores(self) -> list[tuple[str, int]]:
        """Get the player state."""
        return [(player.name, player.diamonds) for player in self._players]

    def add_player(self, name: str) -> bool:
        """Add a player to the game state."""

        for player in self._players:
            if player.name == name:
                return False

        self._players.append(Player(name, self._redis))
        return True

    def player_kick(self, name: str) -> bool:
        """Kick a player from the game state."""
        for player in self._players:
            if player.name == name:
                player.delete()
                self._players.remove(player)
                return True
        
        return False

    def player_remove_all(self) -> None:
        """Remove all players from the game state."""
        for player in self._players:
            player.delete()
        self._players = []

    def reset_diamonds(self) -> None:
        """Reset the diamonds of all players to 0."""
        for player in self._players:
            player.diamonds = 0

    def flush_redis(self) -> None:
        """Remove all entries from redis."""
        self.player_remove_all()
        self._redis.flushdb()

    # endregion ------ admin -----
    # region ----- player -----

    def get_player_names(self) -> list[str]:
        """Get a list of player names."""
        return [player.name for player in self._players]

    def get_player_diamonds(self, name: str) -> int:
        """Get the number of diamonds for a player."""
        for player in self._players:
            if player.name == name:
                return player.diamonds

        raise ValueError("Player not found")

    def add_diamonds(self, name: str, amount: int) -> int:
        """Add a diamond state to the game state."""
        for player in self._players:
            if player.name != name:
                continue
            
            player.diamonds += amount
            return player.diamonds

        raise ValueError("Player not found")

    def remove_diamonds(self, name: str, amount: int) -> int:
        """Remove a diamond state from the game state."""
        for player in self._players:
            if player.name != name:
                continue

            if player.diamonds - amount <= 0:
                player.diamonds = 0
            else:
                player.diamonds -= amount
            return player.diamonds
        raise ValueError("Player not found")

    # endregion ----- player -----



GAME_STATE = GameState()