/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import { useEffect, useState } from "react";
import type { IPlayer } from "~/@types/state";
import { BaseLayout } from "~/components/baselayout";

interface MenuProps {
  setPlayer: React.Dispatch<React.SetStateAction<IPlayer | null>>;
}

export const Menu: React.FunctionComponent<MenuProps> = ({ setPlayer }) => {
  const [availablePlayers, setAvailablePlayer] = useState<IPlayer[]>([]);

  useEffect(() => {
    fetch(encodeURI(`http://localhost:8000/state`), {
      method: "GET",
      headers: {
        accept: "application/json",
      },
    }).then(async (response) => {
      if (response.status !== 200) return console.error("EEEERRRORORR");

      const responseBody = (await response.json()).players;

      setAvailablePlayer(
        Object.keys(responseBody).map((name) => ({
          name,
          score: responseBody[name],
        })),
      );
    });
  }, []);

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
