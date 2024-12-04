/*
 * Copyright (C) 2024 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

// @deno-types="npm:@types/express"
import express from "npm:express";

const app = express();

enum Player {
  hannah = "hannah",
  esra = "esra",
  max = "max",
  peter = "peter",
  marie = "marie",
}

const state: Map<string, number> = new Map([
  [Player.hannah, 3],
  [Player.esra, 0],
  [Player.max, 0],
  [Player.peter, 0],
  [Player.marie, 0],
]);

for (const player in Player) {
  app.get(`/api/${player}`, (req, res) => {
    console.log("Requested state for player " + player + ". State is " + state.get(player));
    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });
}

app.use("/players", express.static("players"));
app.listen(8080);
