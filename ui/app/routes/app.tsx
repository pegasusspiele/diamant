/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import { useState } from "react";
import type { IPlayer } from "~/@types/state";
import { Menu } from "~/components/menu";
import { Player } from "../components/player";
import type { Route } from "./+types/app";

export function meta({}: Route.MetaArgs) {
  return [{ title: "CONspiracy" }, { name: "description", content: "Made with love at Pegasus Spiele HQ" }];
}

export default function App() {
  const nico: IPlayer = {
    name: "Nico",
    score: 10,
  };

  const [player, setPlayer] = useState<IPlayer | null>(null);

  if (!player) return <Menu setPlayer={(player) => setPlayer(player)} />;

  return (
    <Player
      player={player}
      updateScore={(newScore: number) => setPlayer({ ...player, score: newScore })}
      exit={() => setPlayer(null)}
    />
  );
}
