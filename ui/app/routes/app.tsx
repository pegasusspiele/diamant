/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

import { useState } from "react";
import type { Player } from "~/@types/state";
import { PlayerScreen } from "../PlayerScreen/PlayerScreen";
import type { Route } from "./+types/app";

export function meta({}: Route.MetaArgs) {
  return [{ title: "New React Router App" }, { name: "description", content: "Welcome to React Router!" }];
}

export default function App() {
  const [player, setPlayer] = useState<Player>({
    name: "Nico",
    score: null,
  });

  return (
    <PlayerScreen
      player={player}
      setPlayer={setPlayer}
    />
  );
}
