import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import "../App.css";

function Sidebar({ activeTab }) {
  return (
    <aside className="sidebar">
      <div className="logo">
        <img src="/images/logo_new.png" alt="Cropify Logo" />
        <span>Cropify</span>
      </div>

      <nav className="nav-links">
        <Link to="/" className={activeTab === "dashboard" ? "active" : ""}>
          <span className="material-icons">dashboard</span> Dashboard
        </Link>
        {/* <Link to="/model" className={activeTab === "model" ? "active" : ""}>
          <span className="material-icons">insights</span> Prediction Model
        </Link> */}
        <Link to="/analytics" className={activeTab === "analytics" ? "active" : ""}>
          <span className="material-icons">analytics</span> Analytics
        </Link>
        <Link to="/datasets" className={activeTab === "datasets" ? "active" : ""}>
          <span className="material-icons">dataset</span> Datasets
        </Link>
        <Link to="/logs" className={activeTab === "logs" ? "active" : ""}>
          <span className="material-icons">bug_report</span> Logs & Errors
        </Link>
        <Link to="/settings" className={activeTab === "settings" ? "active" : ""}>
          <span className="material-icons">settings</span> Settings
        </Link>
      </nav>

      {/* <div className="feedback-box">
        <button>About Dev</button>
        <br />
        <a
          href="https://kartikdixit.vercel.app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Kartikdixit.vercel.app
        </a>
      </div> */}
    </aside>
  );
}

Sidebar.propTypes = {
  activeTab: PropTypes.oneOf([
    "dashboard",
    "model",
    "analytics",
    "datasets",
    "logs",
    "settings",
  ]).isRequired,
};

export default Sidebar;
