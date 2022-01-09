import React from "react";
import { shallow } from "enzyme";
import LoanList from "./loan-list.component";

import Enzyme from "enzyme";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

let wrapper;
beforeEach(() => {
  const mockProps = {
    loans: [
      {
        contract_date: "2020-05-31",
        current_balance: 3197.35,
        first_name: "Hui",
        id: 1,
        interest_rate: 0.075,
        last_name: "Zamorano",
        lender_id: 1,
        loan_amount: 5000,
        loan_term: 48,
        monthly_payment: 120.89,
        number_payments: 19,
      },
      {
        contract_date: "2020-05-31",
        current_balance: 6278.4,
        first_name: "Wilma",
        id: 2,
        interest_rate: 0.05,
        last_name: "Cecena",
        lender_id: 1,
        loan_amount: 10000,
        loan_term: 48,
        monthly_payment: 230.29,
        number_payments: 19,
      },
    ],
  };

  wrapper = shallow(<LoanList {...mockProps} />);
});

it("should render LoanList component", () => {
  expect(wrapper).toMatchSnapshot();
});
