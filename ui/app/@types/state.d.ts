/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

export type Player = {
  name: string;
  score: number | null;
};

export type State = {
  players: {
    [name: string]: Player;
  };
};
