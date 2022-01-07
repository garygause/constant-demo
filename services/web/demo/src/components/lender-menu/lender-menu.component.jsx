import React from "react";

import LenderMenuItem from "../lender-menu-item/lender-menu-item.component";

import "./lender-menu.styles.scss";

class LenderMenu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lenders: props.lenders,
    };
  }

  render() {
    return (
      <div className="lender-menu">
        {this.props.lenders.map((lender) => (
          <LenderMenuItem key={lender.id} lender={lender} />
        ))}
      </div>
    );
  }
}

export default LenderMenu;
