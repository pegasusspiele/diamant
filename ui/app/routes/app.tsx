/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import { useEffect, useState } from "react";
import { v4 } from "uuid";
import type { IPlayer } from "~/@types/state";
import { BaseLayout } from "~/components/baselayout";
import type { Route } from "./+types/app";

export function meta({}: Route.MetaArgs) {
  return [{ title: "CONspiracy" }, { name: "description", content: "Made with love at Pegasus Spiele HQ" }];
}

export default function App() {
  const [availablePlayers, setAvailablePlayer] = useState<IPlayer[]>([]);

  const uuid = v4();
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
        console.log(typedMessage);
        setAvailablePlayer(typedMessage);
      }
    };
  }, [ws]);

  function updatePlayerName(name: string) {
    if (!ws) return;

    ws.send(
      JSON.stringify({
        msg: {
          RenameMessage: "RenameMessage",
          name,
        },
      }),
    );
  }

  return (
    <BaseLayout>
      {availablePlayers
        .sort((a, b) => a.name.localeCompare(b.name))
        .map(({ name }, idx) => (
          <button
            key={idx}
            onClick={() => updatePlayerName(name)}
          >
            {name}
          </button>
        ))}
    </BaseLayout>
  );

  // const [player, setPlayer] = useState<IPlayer | null>(null);

  // if (!player) return <Menu setPlayer={(player) => setPlayer(player)} />;

  // return (
  //   <Player
  //     player={player}
  //     updateScore={(newScore: number) => setPlayer({ ...player, score: newScore })}
  //     exit={() => setPlayer(null)}
  //   />
  // );
}

/*
{
  msg: {
    RenameMessage: "RenameMessage",
    name: "new Name ..."
  }
}
*/
