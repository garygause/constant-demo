import React from "react";
import { Route } from "react-router-dom";

import LenderMenu from "../../components/lender-menu/lender-menu.component";
import LoansContainer from "../../components/loans-container/loans-container.component";

import "./dashboardpage.styles.scss";

class DashboardPage extends React.Component {
  constructor() {
    super();
    this.state = {
      lenders: [],
      error: null,
    };
  }

  componentDidMount() {
    fetch("http://localhost:1337/api/lenders")
      .then((res) => res.json())
      .then(
        (result) => {
          this.setState({
            lenders: result,
          });
        },
        (error) => {
          this.setState({
            error,
          });
        }
      );
  }

  render() {
    const { lenders } = this.state;
    return (
      <div className="dashboardpage">
        <LenderMenu lenders={lenders} />
        <Route
          exact
          path="/loans/:lenderId/"
          render={(props) => <LoansContainer {...props} lenders={lenders} />}
        />
      </div>
    );
  }
}

export default DashboardPage;
