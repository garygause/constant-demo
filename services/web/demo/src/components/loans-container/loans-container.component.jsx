import React from "react";

import LenderDetails from "../lender-details/lender-details.component";
import LoanList from "../loan-list/loan-list.component";

class LoansContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      loans: [],
    };
  }

  componentDidMount() {
    fetch(`http://localhost:1337/api/loans`)
      .then((res) => res.json())
      .then(
        (result) => {
          this.setState({
            loans: result,
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
    const { loans } = this.state;
    const lenderId = this.props.match.params.lenderId;
    const lenders = this.props.lenders;

    // since this is just a demo and the data won't change
    // let's just filter the data by lender id
    const lender = lenders.find(({ id }) => id == lenderId);
    const filteredLoans = loans.filter((loan) => loan.lender_id == lenderId);

    if (typeof lender == "undefined") {
      return (
        <div className="loanscontainer">
          <span>Error: Lender not found.</span>
        </div>
      );
    } else {
      return (
        <div className="loanscontainer">
          <LenderDetails lender={lender} />
          <LoanList loans={filteredLoans} />
        </div>
      );
    }
  }
}

export default LoansContainer;
