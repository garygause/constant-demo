import React from "react";
import { Link } from "react-router-dom";

import { ReactComponent as Logo } from "../../assets/crown.svg";

import "./header.styles.scss";

const Header = ({ title }) => (
  <div className="header">
    <div className="logo-container">
      <Link to="/">
        <Logo />
      </Link>
    </div>
    <h1 className="title">{title}</h1>
  </div>
);

export default Header;
