/*
 * Copyright (C) 2024 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

// @deno-types="npm:@types/express"
import express from "npm:express";
const app = express();

// @deno-types="npm:@types/express-ws"
import expressWs from "npm:express-ws";
expressWs(app);

enum Player {
  hannah = "hannah",
  esra = "esra",
  max = "max",
  peter = "peter",
  marie = "marie",
}

const initialState: Iterable<readonly [Player, number]> = [
  [Player.hannah, 0],
  [Player.esra, 0],
  [Player.max, 0],
  [Player.peter, 0],
  [Player.marie, 0],
];

const state: Map<string, number> = new Map(initialState);

const sockets: any = [];

function sendState() {
  for (const socket of sockets) {
    socket.send(JSON.stringify(Object.fromEntries(state.entries())));
  }
}

function addWS(ws: any) {
  sockets.push(ws);
  sendState();
}

app.ws("/api/director", (ws, req) => {
  addWS(ws);
});

app.get("/", (_req, res) => res.redirect("/players"));

for (const player in Player) {
  app.get(`/api/${player}`, (_req, res) => {
    console.log("Requested state for player " + player + ". State is " + state.get(player));
    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
  });

  app.post(`/api/${player}/plus`, (_req, res) => {
    const currentState = state.get(player);
    state.set(player, currentState! + 1);

    console.log("Updating state for player " + player + ". State plus one => " + (currentState! + 1));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
    sendState();
  });

  app.post(`/api/${player}/minus`, (_req, res) => {
    const currentState = state.get(player);

    // player state is bound to min zero
    if (currentState! <= 0) {
      res.set("Content-Type", "text/html");
      res.send("" + 0);
      state.set(player, 0);
      sendState();
      return;
    }

    state.set(player, currentState! - 1);

    console.log("Updating state for player " + player + ". State minus one => " + (state.get(player)! - 1));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
    sendState();
  });

  app.post(`/api/${player}/plusTen`, (_req, res) => {
    const currentState = state.get(player);
    state.set(player, currentState! + 10);

    console.log("Updating state for player " + player + ". State plus ten => " + (currentState! + 10));

    res.set("Content-Type", "text/html");
    res.send("" + state.get(player));
    sendState();
  });

  app.post(`/api/${player}/minusTen`, (_req, res) => {
    const currentState = state.get(player);

    // player state is bound to min zero
    if (currentState! - 10 <= 0) {
      res.set("Content-Type", "text/html");
      res.send("" + 0);
      state.set(player, 0);

      console.log("Can't update state for player " + player + ". State would less or equals zero, setting to 0");

      sendState();
      return;
    } else {
      state.set(player, currentState! - 10);

      console.log("Updating state for player " + player + ". State minus ten => " + (state.get(player)! - 10));

      res.set("Content-Type", "text/html");
      res.send("" + state.get(player));
      sendState();
    }
  });
}

app.use("/players", express.static("players"));
app.use("/director", express.static("director"));

app.listen(8080);
