#
# Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#

from models import GameState
from models.PlayerDTO import PlayerDTO
from models.messages.StateMessage import StateMessage
from services.player_websocket_service import PLAYER_WEBSOCKET_SERVICE


def StateMessage_of_GameState(gameState: GameState) -> StateMessage:
    state = gameState.get_player_scores()
    return StateMessage(state=[ PlayerDTO(name=name, diamonds=diamonds, isAlive=PLAYER_WEBSOCKET_SERVICE.is_alive(name)) for (name, diamonds) in state ])