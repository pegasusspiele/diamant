#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from fastapi import APIRouter

from models.messages.ReloadMessage import ReloadMessage
from models.messages.StateMessage import StateMessage
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE
from models.messages.Message import Message

router = APIRouter()

@router.get("/")
async def get_state():
    await PLAYER_WEBSOCKET_SERVICE.notify_all(Message(msg=StateMessage()))
    return {"message": "Admin endpoint"}
