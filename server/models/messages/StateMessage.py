#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from pydantic import BaseModel, Field
from models.PlayerDTO import PlayerDTO

class StateMessage(BaseModel):
    StateMessage: str = Field(default="StateMessage")
    state: list[PlayerDTO] = Field(default=[])



