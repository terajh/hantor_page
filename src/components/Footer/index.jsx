import React from "react";
import './style.css'
const Footer = () => {
  return (
    <footer className="main_footer">
      <div className="container_outer clearfix text-center">
        <div className="copy eng">
          Copyright ⓒ 2021 by Hantor. All Rights Reserved.
          <br className="visible-xs" /> Hantor is a{" "}
          <span className="fcBlue">Ajou University</span>.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
