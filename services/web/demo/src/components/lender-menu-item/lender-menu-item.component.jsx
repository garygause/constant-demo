import React from "react";
import { Link } from "react-router-dom";

import "./lender-menu-item.styles.scss";

const LenderMenuItem = ({ lender }) => (
  <div className="lender-menu-item">
    <Link to={`/loans/${lender.id}/`} className="lender-link">
      {lender.name}
    </Link>
  </div>
);

export default LenderMenuItem;
