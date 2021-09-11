import React, { useState } from "react";

import "../css/navbar.css";
import { NavLink } from "react-router-dom";
import { GiHamburgerMenu } from "react-icons/gi";
import { AiOutlineClose } from "react-icons/ai";
export default function Navbar() {
    const [close, setClose] = useState(false);
    const closeHandler = () => {
        setClose(!close);
    };
    return (
        <div className="navbar">
            <div className="logo">StlViewer</div>

            <div className={close ? "links activated" : "links"}>
                <NavLink className="navlink" activeClassName="active" to="/">
                    Home
                </NavLink>

            </div>

            <div className="hamburger">
                {!close ? (
                    <GiHamburgerMenu className="hamburger_btn" onClick={closeHandler} />
                ) : (
                    <AiOutlineClose className="hamburger_btn" onClick={closeHandler} />
                )}
            </div>
        </div>
    );
}
