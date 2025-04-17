#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import player, admin, websocket, state

APP_MODE = os.environ.get("APP_MODE", "dev")
docs_url = None if APP_MODE == "production" else "/docs"
redoc_url = None if APP_MODE == "production" else "/redoc"  
openapi_url = None if APP_MODE == "production" else "/openapi.json"

app = FastAPI(docs_url=docs_url, redoc_url=redoc_url, openapi_url=openapi_url)
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
