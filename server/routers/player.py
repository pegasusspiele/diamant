#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from fastapi import APIRouter
from models.GameState import GAME_STATE
from models.messages.Message import Message
from services.admin_websocket_service import ADMIN_WEBSOCKET_SERVICE
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE
from util import StateMessage_of_GameState

router = APIRouter()

@router.get("/")
def get_players() -> list[str]:
    return GAME_STATE.get_player_names()


@router.post("/{name}/diamonds")
async def update_diamonds(name: str, diamonds: int) -> None:
    if diamonds < 0:
        GAME_STATE.remove_diamonds(name, abs(diamonds))
    else:
        GAME_STATE.add_diamonds(name, diamonds)

    await PLAYER_WEBSOCKET_SERVICE.notify_all(
        Message(msg=StateMessage_of_GameState(GAME_STATE))
    )
    await ADMIN_WEBSOCKET_SERVICE.notify_all(
        Message(msg=StateMessage_of_GameState(GAME_STATE))
    )
