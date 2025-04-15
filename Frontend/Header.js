import React from "react";
import { Link } from "react-scroll";
import "./Header.css";

const Header = () => {
    return (
        <header className="header">
            <div className="header-container">
                <div className="logo-container">
                    <div className="logo-icon">🔬</div>
                    <h1 className="logo-text">
                        <span className="logo-primary">Derma</span>
                        <span className="logo-secondary">AI</span>
                    </h1>
                </div>
                
                <nav className="nav-menu">
                    <ul className="nav-list">
                        <li className="nav-item">
                            <Link to="home" smooth={true} duration={500}
                                className="nav-link"
                                activeClass="active-link">
                                Home
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="detection" smooth={true} duration={500}
                                className="nav-link"
                                activeClass="active-link">
                                Skin Analysis
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="experts" smooth={true} duration={500}
                                className="nav-link"
                                activeClass="active-link">
                                Find Experts
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="contact" smooth={true} duration={500}
                                className="nav-link"
                                activeClass="active-link">
                                Contact
                            </Link>
                        </li>
                    </ul>
                </nav>
                
                <button className="cta-button">
                    Get Started
                </button>
            </div>
        </header>
    );
};

export default Header;