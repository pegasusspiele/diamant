/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH
 * Use of this source code is governed by an MIT-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/MIT.
 */

import type React from "react";

interface BaseLayoutProps {
  children: React.ReactNode;
  onLogoClick?: () => void;
}

export const BaseLayout: React.FunctionComponent<BaseLayoutProps> = ({ children, onLogoClick }) => (
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
    {children}
    <div id="credits">
      Made with <span id="love">❤</span> by your colleagues
    </div>
  </div>
);
