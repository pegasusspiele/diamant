/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import type { IPlayer } from "~/@types/state";

interface PlayerProps {
  player: IPlayer;
  exit: () => void;
}

export const Player: React.FunctionComponent<PlayerProps> = ({ player, exit }) => {
  function update(delta: 1 | 10 | -1 | -10) {
    fetch(encodeURI(`http://localhost:8000/api/player/${player.name}/diamonds?diamonds=${delta}`), {
      method: "POST",
      headers: {
        accept: "application/json",
      },
    }).then(async (response) => {
      if (response.status !== 200) return console.error("EEEERRRORORR");

      // updatePlayer(await response.text());
    });
  }

  return (
    <>
      <div id="playerNameContainer">
        <div id="playerName">{player.name}</div>
      </div>
      <table>
        <tbody>
          <tr>
            <td>
              <div className="buttonContainer">
                <button onClick={() => update(-1)}>-1</button>
                <button onClick={() => update(-10)}>-10</button>
              </div>
            </td>
            <td id="score">{player.diamonds === null ? "#" : player.diamonds}</td>
            <td>
              <div className="buttonContainer">
                <button onClick={() => update(1)}>+1</button>
                <button onClick={() => update(10)}>+10</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </>
  );
};
