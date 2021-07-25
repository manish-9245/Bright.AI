import React from 'react';
import "../assets/css/navbar.css"

const Navbar = () => {

    return (
        <header id="header" className="fixed-top  header-transparent ">
        <div className="container d-flex align-items-center justify-content-between">
    
          <div className="logo">
            <h1><a href="index.html">Bright.AI</a></h1>
          </div>
        <nav id="navbar" className="navbar">
        <ul>
          <li><a className="nav-link scrollto active" href="http://localhost/bright.ai/Welcome%20Page/index.html">Home</a></li>
          <li><a className="nav-link scrollto" href="https://share.streamlit.io/joeljjoseph/bright.ai/main/app.py">Analyze</a></li>
          <li><a className="nav-link scrollto" href="http://localhost:2368/">Blogs</a></li>
          <li><a className="nav-link scrollto" href="/">Consultation</a></li>
          <li><a className="nav-link scrollto" href="https://go.echoar.xyz/datC">AR Skin Model</a></li>
          <li><a className="nav-link scrollto" href="http://localhost/bright.ai/login.php">Login/Signup</a></li>
        </ul>
        <i className="bi bi-list mobile-nav-toggle"></i>
      </nav>
      </div>
      </header>
    )
}

export default Navbar;


			