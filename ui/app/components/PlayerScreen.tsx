/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

import { useEffect } from "react";
import type { Player } from "~/@types/state";
import { BaseLayout } from "~/components/baselayout";

interface PlayerScreenProps {
  player: Player;
  updateScore: (newScore: number) => void;
  exit: () => void;
}

export const PlayerScreen: React.FunctionComponent<PlayerScreenProps> = ({ player, updateScore, exit }) => {
  function updatePlayer(_newScore: string) {
    const newScore = Number(_newScore);

    if (typeof newScore !== "number") return console.error("newScore not number");

    updateScore(newScore);
  }

  useEffect(() => {
    fetch(encodeURI(`http://localhost:8000/player/${player.name}`), {
      method: "GET",
      headers: {
        accept: "application/json",
      },
    }).then(async (response) => {
      if (response.status !== 200) return console.error("EEEERRRORORR");

      updatePlayer(await response.text());
    });
  }, []);

  function update(delta: 1 | 10 | -1 | -10) {
    fetch(encodeURI(`http://localhost:8000/player/${player.name}/diamonds?diamonds=${delta}`), {
      method: "PUT",
      headers: {
        accept: "application/json",
      },
    }).then(async (response) => {
      if (response.status !== 200) return console.error("EEEERRRORORR");

      updatePlayer(await response.text());
    });
  }

  return (
    <BaseLayout onLogoClick={() => exit()}>
      <table>
        <tbody>
          <tr>
            <td>
              <div className="buttonContainer">
                <button onClick={() => update(-1)}>-1</button>
                <button onClick={() => update(-10)}>-10</button>
              </div>
            </td>
            <td id="score">{player.score === null ? "#" : player.score}</td>
            <td>
              <div className="buttonContainer">
                <button onClick={() => update(1)}>+1</button>
                <button onClick={() => update(10)}>+10</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div id="credits">
        Made with <span id="love">❤</span> by your colleagues
      </div>
    </BaseLayout>
  );
};
