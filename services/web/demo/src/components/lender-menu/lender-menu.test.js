import React from "react";
import { shallow } from "enzyme";
import LenderMenu from "./lender-menu.component";

import Enzyme from "enzyme";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

let wrapper;
beforeEach(() => {
  const mockProps = {
    lenders: [
      {
        id: 1,
        name: "test",
        address: "123",
        city: "Seattle",
        state: "WA",
        zip: "98115",
      },
      {
        id: 2,
        name: "test",
        address: "123",
        city: "Seattle",
        state: "WA",
        zip: "98115",
      },
    ],
  };

  wrapper = shallow(<LenderMenu {...mockProps} />);
});

it("should render LenderMenu component", () => {
  expect(wrapper).toMatchSnapshot();
});
