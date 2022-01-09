import React from "react";
import { shallow } from "enzyme";
import DashboardPage from "./dashboardpage.component";

import Enzyme from "enzyme";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

it("should render DashboardPage component", () => {
  expect(shallow(<DashboardPage />)).toMatchSnapshot();
});
