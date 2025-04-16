#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from fastapi import APIRouter
from models.GameState import GAME_STATE
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE
from services.admin_websocket_service import ADMIN_WEBSOCKET_SERVICE
from models.messages.Message import Message
from util import StateMessage_of_GameState
from models.GameState import GAME_STATE

router = APIRouter()

@router.post("/trigger-reload")
async def trigger_reload():
    await PLAYER_WEBSOCKET_SERVICE.notify_all(Message(msg=StateMessage_of_GameState(GAME_STATE)))
    await ADMIN_WEBSOCKET_SERVICE.notify_all(
        Message(msg=StateMessage_of_GameState(GAME_STATE))
    )
