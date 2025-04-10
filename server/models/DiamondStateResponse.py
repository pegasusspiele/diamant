from pydantic import BaseModel

class DiamondStateResponse(BaseModel):
    players: dict[str, int]