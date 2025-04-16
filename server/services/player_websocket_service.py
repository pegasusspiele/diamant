#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

import json
from models.messages import Message
from fastapi import WebSocket

class PlayerWebsocketService:
    def __init__(self):
        self._sockets: dict[str, WebSocket] = {}

    def register(self, name: str, socket: WebSocket) -> None:
        if name in self._sockets:
            raise ValueError(f"Socket with name {name} already exists")
        self._sockets[name] = socket

    def unregister(self, name: str) -> None:
        pass
        self._sockets.pop(name, None)

    def is_alive(self, name: Message) -> bool:
        # Check if the socket is still connected
        return name in self._sockets

    async def notify_all(self, message: str) -> None:
        for socket_name in self._sockets:
            await self._sockets[socket_name].send_json(message.dict())

PLAYER_WEBSOCKET_SERVICE = PlayerWebsocketService()
