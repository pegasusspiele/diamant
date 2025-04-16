#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.GameState import GameState

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = GameState()

@app.get("/")
def root():
    return {"message": "Hello World"}

state.add_player("Cedric")
state.add_player("Cedric")

# @app.websocket("/ws/player/{name}")
# async def websocket_endpoint(name: str, websocket: WebSocket):
#     await websocket.accept()

#     if name not in player:
#         await websocket.close(code=1007, reason="player not existent")
#         return

#     score, _ = player[name]
#     player[name] = (score, websocket)
#     await notify_admin()

#     try:
#         while True:
#             await websocket.receive_text()
#     except:
#         print(f"websocket connection to player {name} closed")
#     finally:
#         player[name] = (score, None)
#         await notify_admin()

# @app.websocket("/ws/admin")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     global admin
#     if admin is not None:
#         await websocket.close(code=1007, reason="admin already connected")
#         return
#     admin = websocket
#     try:
#         while True:
#             await websocket.receive_text()
#     except:
#         print(f"websocket connection to admin closed")
#     finally:
#         admin = None
