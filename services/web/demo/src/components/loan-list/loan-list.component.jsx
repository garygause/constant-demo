import React from "react";

import "./loan-list.styles.scss";

const LoanList = ({ loans }) => {
  // reqs doc said to convert 0.75 to 7.5% but that seems wrong
  // so doing the standard 0.075 to 7.5% to match data
  const formatRate = (value) => {
    return `${value * 100}%`;
  };

  const formatCurrency = (value) => {
    return "$" + value.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
  };

  // we don't know if the date should be locallized at all
  // assume not
  const formatDate = (value) => {
    const date = value.substring(0, 10).split("-");
    return `${date[1]}/${date[2]}/${date[0]}`;
  };

  const formattedLoans = loans.map((loan) => {
    return {
      ...loan,
      interest_rate: formatRate(loan.interest_rate),
      loan_amount: formatCurrency(loan.loan_amount),
      current_balance: formatCurrency(loan.current_balance),
      monthly_payment: formatCurrency(loan.monthly_payment),
      contract_date: formatDate(loan.contract_date),
    };
  });

  return (
    <div className="loan-list">
      <h2 className="title">Loans</h2>
      <table className="loan-table">
        <thead>
          <tr>
            <td>First Name</td>
            <td>Last Name</td>
            <td>Interest Rate</td>
            <td>Loan Amount</td>
            <td>Current Balance</td>
            <td>Term</td>
            <td># Payments Made</td>
            <td>Mo. Pymnt</td>
            <td>Contract Date</td>
          </tr>
        </thead>
        <tbody>
          {formattedLoans.map((loan) => (
            <tr key={loan.id}>
              <td>{loan.first_name}</td>
              <td>{loan.last_name}</td>
              <td className="center">{loan.interest_rate}</td>
              <td>{loan.loan_amount}</td>
              <td>{loan.current_balance}</td>
              <td className="center">{loan.loan_term}</td>
              <td className="center">{loan.number_payments}</td>
              <td>{loan.monthly_payment}</td>
              <td>{loan.contract_date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LoanList;
