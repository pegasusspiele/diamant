#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
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
