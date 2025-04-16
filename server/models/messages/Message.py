#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
#

from typing import Union
from pydantic import BaseModel
from models.messages.ReloadMessage import ReloadMessage
from models.messages.StateMessage import StateMessage

class Message(BaseModel):
    msg: Union[ReloadMessage, StateMessage]