import React from "react";
import { Route } from "react-router-dom";

import Header from "./components/header/header.component";
import DashboardPage from "./pages/dashboardpage/dashboardpage.component";

import "./App.css";

const App = () => (
  <div>
    <Header title="Constant Servicer" />
    <Route path="/" component={DashboardPage} />
  </div>
);

export default App;
