#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from fastapi import APIRouter, WebSocket
from services.admin_websocket_service import  ADMIN_WEBSOCKET_SERVICE
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE

router = APIRouter()

@router.websocket("/player/{name}")
async def websocket_endpoint(name: str, websocket: WebSocket):
    try:
        await websocket.accept()
        PLAYER_WEBSOCKET_SERVICE.register(name, websocket)

        while True:
            await websocket.receive_text()
    except:
        print(f"player ({name}) websocket connection closed")
    finally:
        PLAYER_WEBSOCKET_SERVICE.unregister(name)


@router.websocket("/admin")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()    
        ADMIN_WEBSOCKET_SERVICE.register(websocket)
    
        while True:
            await websocket.receive_text()
    except:
        print(f"admin websocket connection closed")
    finally:
       ADMIN_WEBSOCKET_SERVICE.unregister(websocket)
