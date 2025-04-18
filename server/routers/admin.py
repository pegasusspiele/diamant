#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from fastapi import APIRouter, HTTPException
from models.GameState import GAME_STATE
from models.messages.ConfettiMessage import ConfettiMessage
from models.messages.AlertMessage import AlertMessage
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE
from services.admin_websocket_service import ADMIN_WEBSOCKET_SERVICE
from models.messages.Message import Message
from util import StateMessage_of_GameState
from models.GameState import GAME_STATE

router = APIRouter()

async def send_state_update():
    await PLAYER_WEBSOCKET_SERVICE.notify_all(Message(msg=StateMessage_of_GameState(GAME_STATE)))
    await ADMIN_WEBSOCKET_SERVICE.notify_all(
        Message(msg=StateMessage_of_GameState(GAME_STATE))
    )

@router.post("/player/{name}")
async def create_player(name: str):
    success = GAME_STATE.add_player(name)
    
    if success != True:
        raise HTTPException(status_code=409)
    
    await send_state_update()
    
@router.delete("/player/{name}")
async def delete_player(name: str):
    success = GAME_STATE.player_kick(name)
    
    if success != True:
        raise HTTPException(status_code=404)
    
    await send_state_update()
    
@router.delete("/player")
async def delete_all_players():
    GAME_STATE.player_remove_all()
    await send_state_update()

@router.post("/reset-diamonds")
async def reset_diamonds():
    GAME_STATE.reset_diamonds()
    await send_state_update()

@router.post("/trigger-confetti")
async def trigger_confetti():
    await PLAYER_WEBSOCKET_SERVICE.notify_all(Message(msg=ConfettiMessage()))

@router.post("/message")
async def send_message(message: str):
    await PLAYER_WEBSOCKET_SERVICE.notify_all(Message(msg=AlertMessage(text=message)))

@router.post("/message/{player}")
async def send_message(player: str, message: str):
    try:
        await PLAYER_WEBSOCKET_SERVICE.notify(player, Message(msg=AlertMessage(text=message)))
    except ValueError:
        raise HTTPException(status_code=404, detail="Player not found")