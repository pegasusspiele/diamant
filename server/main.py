#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import player, admin, websocket, state

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player.router, prefix="/api/player", tags=["player"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(state.router, prefix="/api/state", tags=["state"])
app.include_router(websocket.router, prefix="/api/ws", tags=["websocket"])
