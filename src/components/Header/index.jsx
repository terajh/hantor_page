import React, { useState, useEffect} from "react";
import logo from "../../assets/comm/logo.png";
import {appendScript} from "../../js/utils/appenScript"

const Header = (props) => {
  const [mod, setMod] = useState('main');

  useEffect(() => {
    if(mod ==='main') appendScript("/start.js");
    appendScript("/main_ui.js");
    return ()=> {
    };
  },[props.mode]);


  return (
    <header
      className="header_main"
      data-aos="fade-down"
      data-aos-easing="ease-out-cubic"
      data-aos-duration="1000"
    >
      <div className="skin_contents">
        <a href="#main_contents">본문바로가기</a>
      </div>
      <h1 className="logo" id="rev-1">
        <a href="#" onClick={()=>{
          setMod('main');
          props.changeMode('main');
        }}>
          <img
            src={logo}
            className="wp100"
            style={{ maxWidth: 200 + "px" }}
            alt="hantor"
          />
        </a>
      </h1>
      <div className="container_outer">
        <nav className="eng clearfix">
          <ul className="list-unstyled">
            <li id="01">
              <a href="#" onClick={()=>{
                setMod('work');
                props.changeMode('work');
              }}>WORK</a>
            </li>
            <li id="02">
              <a href="#" onClick={()=>{
                setMod('about');
                props.changeMode('about');
              }}>ABOUT</a>
            </li>
            <li id="03">
              <a href="#" onClick={()=>{
                setMod('news');
                props.changeMode('news');
              }} >NEWS</a>
            </li>
            <li id="04">
              <a href="#" onClick={()=>{
                setMod('contact');
                props.changeMode('contact');
              }}>CONTACT</a>
            </li>
          </ul>
        </nav>

        <div className="mobile_info  visible-xs mt30">
          <div className="dp-table wp100 mb10">
            <div className="dp-table-cell w60 fw600">TEL.</div>
            <div className="dp-table-cell fw300">000.0000.0000</div>
          </div>
          <div className="dp-table wp100">
            <div className="dp-table-cell w60 fw600">E-mail.</div>
            <div className="dp-table-cell fw300">hantor@hantor.co.kr</div>
          </div>
        </div>

        <a href="#" className="m_menu_close visible-xs">
          <span>메뉴닫기</span>
          <i className="xi-close"></i>
        </a>
      </div>

      <div className="mobile_menu_btn hidden-lg hidden-md hidden-sm">
        <a href="#." className="eng">
          MENU
          <p>
            <span></span>
            <span></span>
            <span></span>
          </p>
        </a>
      </div>
      <script src="./script.js" type="text/javascript"></script>
    </header>
  );
};

export default Header;
