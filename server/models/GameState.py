#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from models.Player import Player
from redis import Redis

class GameState:
    def __init__(self):
        self._redis = Redis(host="127.0.0.1", port=6379, db=0)

        player_names = [str(key).split(":")[1] for key in self._redis.keys("PLAYER:*")]
        self._players: list[Player] = [
            Player(name, self._redis) for name in player_names
        ]

    # region ----- admin -----
    
    def get_player_scores(self) -> dict:
        """Get the player state."""
        return {player.name: player.diamonds for player in self.players}

    def add_player(self, name: str) -> None | ValueError:
        """Add a player to the game state."""

        for player in self._players:
            if player.name == name:
                raise ValueError("Player already exists")

        self._players.append(Player(name, self._redis))

    def player_kick(self, name: str) -> None:
        """Kick a player from the game state."""
        for player in self._players:
            if player.name == name:
                player.delete()
                self._players.remove(player)
                break

    def player_remove_all(self) -> None:
        """Remove all players from the game state."""
        for player in self._players:
            player.delete()
        self._players = []

    def reset_diamonds(self) -> None:
        """Reset the diamonds of all players to 0."""
        for player in self.players:
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

    def get_player_diamonds(self, name: str) -> int | ValueError:
        """Get the number of diamonds for a player."""
        for player in self._players:
            if player.name == name:
                return player.diamonds

        raise ValueError("Player not found")

    def add_diamonds(self, name: str, amount: int) -> int | ValueError:
        """Add a diamond state to the game state."""
        for player in self._players:
            if player.name != name:
                continue
            
            player.diamonds += amount
            return player.diamonds

        raise ValueError("Player not found")

    def remove_diamonds(self, name: str, amount: int) -> int | ValueError:
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