import React from "react";
import { shallow } from "enzyme";
import LenderMenuItem from "./lender-menu-item.component";

import Enzyme from "enzyme";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

let wrapper;
beforeEach(() => {
  const mockProps = {
    lender: {
      id: 1,
      name: "test",
      address: "123",
      city: "Seattle",
      state: "WA",
      zip: "98115",
    },
  };

  wrapper = shallow(<LenderMenuItem {...mockProps} />);
});

it("should render LenderMenuItem component", () => {
  expect(wrapper).toMatchSnapshot();
});
