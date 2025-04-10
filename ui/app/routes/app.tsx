/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

import { useState } from "react";
import type { Player } from "~/@types/state";
import { BaseLayout } from "~/components/baselayout";
import { PlayerScreen } from "../components/PlayerScreen";
import type { Route } from "./+types/app";

export function meta({}: Route.MetaArgs) {
  return [{ title: "CONspiracy" }, { name: "description", content: "Made with love at Pegasus Spiele HQ" }];
}

export default function App() {
  const nico: Player = {
    name: "Nico",
    score: 10,
  };

  const [player, setPlayer] = useState<Player | null>(nico);

  if (!player) return <BaseLayout>HI</BaseLayout>;

  return (
    <PlayerScreen
      player={player}
      updateScore={(newScore: number) => setPlayer({ ...player, score: newScore })}
      exit={() => setPlayer(null)}
    />
  );
}
