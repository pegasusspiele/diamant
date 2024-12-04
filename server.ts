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

const initialState: any = [
  [Player.hannah, 0],
  [Player.esra, 0],
  [Player.max, 0],
  [Player.peter, 0],
  [Player.marie, 0],
];

const state: Map<string, number> = new Map(initialState);

for (const player in Player) {
  app.get(`/api/${player}`, (_req, res) => {
    console.log("Requested state for player " + player + ". State is " + state.get(player));
    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });

  app.post(`/api/${player}/plus`, (_req, res) => {
    const currentState = state.get(player);
    state.set(player, currentState! + 1);

    console.log("Updating state for player " + player + ". State minus one => " + (currentState! + 1));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });

  app.post(`/api/${player}/minus`, (_req, res) => {
    const currentState = state.get(player);

    // player state is bound to min zero
    if (currentState! <= 0) {
      res.set("Content-Type", "text/html");
      res.send("" + 0);
      state.set(player, 0);
      return;
    }

    state.set(player, currentState! - 1);

    console.log("Updating state for player " + player + ". State plus one => " + (state.get(player)! - 1));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });

  app.post(`/api/${player}/plusTen`, (_req, res) => {
    const currentState = state.get(player);
    state.set(player, currentState! + 10);

    console.log("Updating state for player " + player + ". State minus ten => " + (currentState! + 10));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });

  app.post(`/api/${player}/minusTen`, (_req, res) => {
    const currentState = state.get(player);

    // player state is bound to min zero
    if (currentState! - 10 < 0) {
      res.set("Content-Type", "text/html");
      res.send("" + 0);
      state.set(player, 0);
      return;
    }

    state.set(player, currentState! - 10);

    console.log("Updating state for player " + player + ". State plus ten => " + (state.get(player)! - 10));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });
}

app.use("/players", express.static("players"));
app.listen(8080);
