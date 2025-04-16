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
    def name(self) -> str:
        return self._name

    @property
    def diamonds(self) -> int:
        res = self._store.get(f"PLAYER:{self._name}:diamonds")
        res = int(res) if res else 0
        return res

    @diamonds.setter
    def diamonds(self, value: int):
        self._store.set(f"PLAYER:{self._name}:diamonds", value)

    def delete(self) -> bool:
        self._store.delete(f"PLAYER:{self._name}:*")
