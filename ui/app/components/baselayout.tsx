/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import type React from "react";
import Confetti from "react-confetti";

interface BaseLayoutProps {
  children: React.ReactNode;
  onLogoClick?: () => void;
  confettiActive: Boolean;
  onConfettiComplete?: () => void;
}

export const BaseLayout: React.FunctionComponent<BaseLayoutProps> = ({ children, onLogoClick, confettiActive, onConfettiComplete }) => (
  <div className="all">
    <div
      id="logoContainer"
      onClick={onLogoClick ? () => onLogoClick() : undefined}
    >
      <img
        id="logo"
        src="logo.png"
      />
    </div>
    {confettiActive && (
      <Confetti
        // fixme: tuning needed
        width={2500}
        height={2500}
        recycle={false}
        onConfettiComplete={onConfettiComplete}
        drawShape={(ctx) => {
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.bezierCurveTo(0, -15, -25, -15, -25, 0); // -3 → -15, -5 → -25
          ctx.bezierCurveTo(-25, 15, 0, 25, 0, 35); //  3 → 15,  5 → 25,  7 → 35
          ctx.bezierCurveTo(0, 25, 25, 15, 25, 0);
          ctx.bezierCurveTo(25, -15, 0, -15, 0, 0);
          ctx.closePath();
          ctx.fillStyle = "#ff0000";
          ctx.fill();
        }}
      />
    )}
    {children}
    <div id="credits">
      Made with <span id="love">❤</span> by your colleagues
    </div>
  </div>
);
