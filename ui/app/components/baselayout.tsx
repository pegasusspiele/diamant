/*
 * Copyright (C) 2025 Pegasus Spiele Verlags- und Medienvertriebsgesellschaft mbH, all rights reserved.
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
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
