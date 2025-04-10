from functools import wraps
import json
from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware


from models.DiamondStateResponse import DiamondStateResponse

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

player : dict[str, tuple[int, WebSocket]] = {}
admin : WebSocket = None

with open("state.json", "r") as f:
    state = json.load(f)
    for name in state:
        player[name] = (state[name], None)

@app.get("/state", tags=["admin"])
def get_player_state() -> DiamondStateResponse:
    return DiamondStateResponse(players = dict([(name, player[name][0]) for name in player]))

@app.get("/player", tags=["player"])
def get_players() -> list[str]:
    return player.keys()

@app.get("/player/{name}", tags=["player"])
def get_player(name: str) -> int:
    if name not in player:
        raise HTTPException(status_code=404)
    return player[name][0]

@app.delete("/player", tags=["admin"])
async def delete_player() -> None:
    global player 
    player = {}
    with open("state.json", "w") as f:
        json.dump(dict([(name, player[name][0]) for name in player]), f)
    await notify_admin()
    return None

@app.delete("/player/{name}", tags=["admin"])
async def delete_player_by_name(name: str) -> None:
    if name not in player:
        raise HTTPException(status_code=404)
    player.pop(name, None)
    with open("state.json", "w") as f:
        json.dump(dict([(name, player[name][0]) for name in player]), f)
    await notify_admin()
    return None

@app.post("/player/{name}", tags=["admin"])
async def create_player(name: str) -> None:
    if name in player:
        raise HTTPException(status_code=400, detail="Player already exists")
    player[name] = (0, None)
    with open("state.json", "w") as f:
        json.dump(dict([(name, player[name][0]) for name in player]), f)
    await notify_admin()

@app.put("/player/{name}/diamonds", tags=["player"])
async def change_diamonds(name: str, diamonds: int) -> int:
    if name not in player: 
        raise HTTPException(status_code=404)
    if diamonds < 0:
        if player[name][0] < -diamonds:
            player[name] = (0, player[name][1])
        else:
            player[name] = (player[name][0] + diamonds, player[name][1])
    else:
        player[name] = (player[name][0] + diamonds, player[name][1])

    with open("state.json", "w") as f:
            json.dump(dict([(name, player[name][0]) for name in player]), f)
    await notify_admin()
    return player[name][0]

@app.post("/admin/reset", tags=["admin"])
async def reset() -> None:
    for name in player:
        player[name] = (0, player[name][1])
    with open("state.json", "w") as f:
        json.dump(dict([(name, player[name][0]) for name in player]), f)
    await notify_players({"action": "reset"})
    await notify_admin()
    return None

async def notify_players(msg: dict[str, any]) -> None:
    for name in player:
        if player[name][1] is not None:
            await player[name][1].send_text(json.dumps(msg))

async def notify_admin() -> None:
    if admin is not None:
        payload = [{"name": name, "diamonds": player[name][0], "alive": player[name][1] is not None} for name in player]
        await admin.send_text(json.dumps(payload))

@app.websocket("/ws/player/{name}")
async def websocket_endpoint(name: str, websocket: WebSocket):
    await websocket.accept()

    if name not in player:
        await websocket.close(code=1007, reason="player not existent")
        return

    score, _ = player[name]
    player[name] = (score, websocket)
    await notify_admin()

    try:
        while True:
            await websocket.receive_text()
    except:
        print(f"websocket connection to player {name} closed")
    finally:
        player[name] = (score, None)
        await notify_admin()

@app.websocket("/ws/admin")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global admin
    if admin is not None:
        await websocket.close(code=1007, reason="admin already connected")
        return
    admin = websocket
    try:
        while True:
            await websocket.receive_text()
    except:
        print(f"websocket connection to admin closed")
    finally:
        admin = None