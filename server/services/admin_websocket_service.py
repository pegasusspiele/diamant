#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from models.messages import Message
from fastapi import WebSocket

class AdminWebsocketService:
    def __init__(self):
        self._sockets: list[WebSocket] = []

    def register(self, socket: WebSocket) -> None:
        self._sockets.append(socket)

    def unregister(self, socket: WebSocket) -> None:
        self._sockets.remove(socket)

    async def notify_all(self, message: Message) -> None:
        for socket in self._sockets:
            await socket.send_json(message)

ADMIN_WEBSOCKET_SERVICE = AdminWebsocketService()
