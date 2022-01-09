import React from "react";
import { shallow } from "enzyme";
import Header from "./header.component";

import Enzyme from "enzyme";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

it("should render Header component", () => {
  expect(shallow(<Header />)).toMatchSnapshot();
});
