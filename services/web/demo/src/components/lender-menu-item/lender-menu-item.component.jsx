import React from "react";

import "./lender-menu-item.styles.scss";

const LenderMenuItem = ({ lender }) => (
  <div className="lender-menu-item">
    <span className="title">{lender.title}</span>
  </div>
);

export default LenderMenuItem;
