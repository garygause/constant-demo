import React from "react";

import LenderMenu from "../../components/lender-menu/lender-menu.component";
import LoanList from "../../components/loan-list/loan-list.component";

import "./homepage.styles.scss";

// test data
import LENDER_DATA from "./lender.data";

const HomePage = () => (
  <div className="homepage">
    <LenderMenu lenders={LENDER_DATA} />
    <LoanList />
  </div>
);

export default HomePage;
