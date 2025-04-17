/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import { useEffect, useId, useState } from "react";
import type { IPlayer } from "~/@types/state";
import { BaseLayout } from "~/components/baselayout";
import { Player } from "~/components/player";
import type { Route } from "./+types/app";

export function meta({}: Route.MetaArgs) {
  return [{ title: "CONspiracy" }, { name: "description", content: "Made with love at Pegasus Spiele HQ" }];
}

export default function App() {
  const [state, setState] = useState<Map<IPlayer["name"], IPlayer>>(new Map());
  const [activePlayer, setActivePlayer] = useState<IPlayer["name"]>();

  const uuid = useId();
  const [ws, setWs] = useState<WebSocket>();

  useEffect(() => {
    setWs(new WebSocket(`http://localhost:8000/api/ws/player/${uuid}`));
  }, []);

  useEffect(() => {
    if (!ws) return;

    ws.onmessage = ({ data }) => {
      const { msg } = JSON.parse(data);

      if (Object.keys(msg).includes("StateMessage")) {
        const typedMessage: IPlayer[] = msg.state;

        if (typedMessage.length < 1) {
          updatePlayer();
        }

        const map: Map<IPlayer["name"], IPlayer> = new Map();
        for (const player of typedMessage) {
          map.set(player.name, player);
        }

        setState(map);
      }
    };
  }, [ws]);

  function updatePlayer(playerName?: IPlayer["name"]) {
    if (!ws) return;
    setActivePlayer(playerName);

    const name = playerName || uuid;
    ws.send(
      JSON.stringify({
        msg: {
          RenameMessage: "RenameMessage",
          name,
        },
      }),
    );
  }

  if (activePlayer && state.get(activePlayer) !== undefined)
    return (
      <Player
        player={state.get(activePlayer)!}
        exit={() => updatePlayer()}
      />
    );

  return (
    <BaseLayout>
      {[...state]
        .map((e) => e[1])
        .sort((a, b) => a.name.localeCompare(b.name))
        .map((player, idx) => (
          <button
            key={idx}
            onClick={() => updatePlayer(player.name)}
          >
            {player.name}
          </button>
        ))}
      <button onClick={() => updatePlayer()}>RESET</button>
    </BaseLayout>
  );
}
