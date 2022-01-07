import React from "react";
import { Route, Switch } from "react-router-dom";

import HomePage from "./pages/homepage/homepage.component";
import Header from "./components/header/header.component";
import { SiteConfig } from "./siteConfig";

import "./App.css";

class App extends React.Component {
  /**
   * Main App file.
   * We expect to have some state stored here so this is a class-based component.
   * We also use Switch because we expect to have more routes than just the home page
   * and Switch is pretty sweet.
   */
  render() {
    return (
      <div>
        <Header title={SiteConfig.TITLE} />
        <Switch>
          <Route exact path="/" component={HomePage} />
        </Switch>
      </div>
    );
  }
}

export default App;
