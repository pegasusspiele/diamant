/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

export type IPlayer = {
  name: string;
  score: number | null;
};

export type IState = {
  players: {
    [name: string]: IPlayer;
  };
};
