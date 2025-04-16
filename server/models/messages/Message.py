#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from typing import Union
from pydantic import BaseModel
from models.messages.StateMessage import StateMessage

class Message(BaseModel):
    msg: Union[StateMessage]