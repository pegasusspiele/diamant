#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from pydantic import BaseModel, Field

class RenameMessage(BaseModel):
    RenameMessage: str = Field(default="RenameMessage")
    name: str = Field(default="Hannebambel")
