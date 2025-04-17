#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from fastapi import APIRouter, WebSocket
from pydantic import ValidationError
from models.messages.RenameMessage import RenameMessage
from services.admin_websocket_service import  ADMIN_WEBSOCKET_SERVICE
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE
from models.messages.Message import Message
from util import StateMessage_of_GameState
from models.GameState import GAME_STATE
import json

router = APIRouter()

@router.websocket("/player/{uuid}")
async def websocket_endpoint(uuid: str, websocket: WebSocket):
    name = uuid
    
    try:
        await websocket.accept()
        PLAYER_WEBSOCKET_SERVICE.register(uuid, websocket)
        
        await PLAYER_WEBSOCKET_SERVICE.notify_all(Message(msg=StateMessage_of_GameState(GAME_STATE)))
        await ADMIN_WEBSOCKET_SERVICE.notify_all(Message(msg=StateMessage_of_GameState(GAME_STATE)))
        
        while True:
            raw = await websocket.receive_text()
            try:
                
                msg = Message.model_validate(json.loads(raw)).msg
                if isinstance(msg, RenameMessage):
                    print(f"player ({name}) rename to {msg.name}")
                    PLAYER_WEBSOCKET_SERVICE.rename(name, msg.name)
                    name = msg.name
            except ValidationError as e:
                print(e)
    except:
        print(f"player ({name}) websocket connection closed")
    finally:
        PLAYER_WEBSOCKET_SERVICE.unregister(name)

@router.websocket("/admin/{uuid}")
async def websocket_endpoint(uuid: str, websocket: WebSocket):
    try:
        await websocket.accept()    
        ADMIN_WEBSOCKET_SERVICE.register(websocket)

        await ADMIN_WEBSOCKET_SERVICE.notify_all(Message(msg=StateMessage_of_GameState(GAME_STATE)))
    
        while True:
            await websocket.receive_text()
    except:
        print(f"admin {uuid} websocket connection closed")
    finally:
       ADMIN_WEBSOCKET_SERVICE.unregister(websocket)
