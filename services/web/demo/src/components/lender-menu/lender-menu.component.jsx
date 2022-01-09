import React from "react";

import LenderMenuItem from "../lender-menu-item/lender-menu-item.component";

import "./lender-menu.styles.scss";

const LenderMenu = ({ lenders }) => (
  <div className="lender-menu">
    <h3 className="title">Lenders</h3>
    {lenders.map((lender) => (
      <LenderMenuItem key={lender.id} lender={lender} />
    ))}
  </div>
);

export default LenderMenu;
