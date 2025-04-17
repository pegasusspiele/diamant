/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import { useState } from "react";
import type { IPlayer } from "~/@types/state";
import { BaseLayout } from "~/components/baselayout";

interface MenuProps {
  setPlayer: React.Dispatch<React.SetStateAction<IPlayer | null>>;
}

export const Menu: React.FunctionComponent<MenuProps> = ({ setPlayer }) => {
  const [availablePlayers, setAvailablePlayer] = useState<IPlayer[]>([]);

  return (
    <BaseLayout>
      {availablePlayers.map((player, idx) => {
        return (
          <button
            key={idx}
            onClick={() => setPlayer(player)}
          >
            {player.name}
          </button>
        );
      })}
    </BaseLayout>
  );
};
