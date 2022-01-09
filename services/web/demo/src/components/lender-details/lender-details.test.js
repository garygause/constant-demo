import React from "react";
import { shallow } from "enzyme";
import LenderDetails from "./lender-details.component";

import Enzyme from "enzyme";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

let wrapper;
beforeEach(() => {
  const mockProps = {
    lender: {
      name: "test",
      address: "123",
      city: "Seattle",
      state: "WA",
      zip: "98115",
    },
  };

  wrapper = shallow(<LenderDetails {...mockProps} />);
});

it("should render LenderDetails component", () => {
  expect(wrapper).toMatchSnapshot();
});
