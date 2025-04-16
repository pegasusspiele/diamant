#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from pydantic import BaseModel

class PlayerDTO(BaseModel):
    name: str
    diamonds: int
    isAlive: bool
