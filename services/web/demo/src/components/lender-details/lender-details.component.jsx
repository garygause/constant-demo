import React from "react";

import "./lender-details.styles.scss";

const LenderDetails = ({ lender }) => {
  return (
    <div className="lender-details">
      <h2 className="title">Lender Info</h2>
      <div>{lender.name}</div>
      <div>{lender.address}</div>
      <div>
        {lender.city}, {lender.state} {lender.zip}
      </div>
      <div>{lender.phone}</div>
    </div>
  );
};

export default LenderDetails;
