#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from redis import Redis

class Player:
    def __init__(self, name: str, redis: Redis):
        self._name: str = name
        self._store: Redis = redis

    @property
    def diamonds(self) -> int | None:
        res = self._store.get(f"{self._name}:diamonds")
        res = int(res) if res else None
        return res

    @diamonds.setter
    def diamonds(self, value: int):
        pass

    def delete(self) -> bool:
        self._store.delete(f"{self._name}:diamonds")
