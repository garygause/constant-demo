import React from "react";
import { Link } from "react-router-dom";

import { ReactComponent as Logo } from "../../assets/logo.svg";

import "./header.styles.scss";

const Header = ({ title }) => (
  <div className="header">
    <Link className="logo-container" to="/">
      <Logo className="logo" />
    </Link>
    <span className="title">{title}</span>
  </div>
);

export default Header;
