import React, { useState, useEffect } from 'react';
import logo from "../../img/comm/logo.png"


const Header = () => {
  useEffect(() => {
    const script = document.createElement("script");
    script.innerHTML = `         
    (function () {
      // Fake loading.
  
      setTimeout(init, 3000);
  
      function init() {
        document.body.classList.remove('loading');
        //************************ Example 1 - reveal on load ********************************
        var rev1 = new RevealFx(document.querySelector('#rev-1'), {
          revealSettings: {
            bgcolor: '#000000',
            onCover: function (contentEl, revealerEl) {
              contentEl.style.opacity = 1;
            }
          }
        });
        rev1.reveal();
  
  
  
        $('.modal_close_x').on('click', function () {
          $("#video1").attr("src", "");
        });
  
        $('.modal_close_x2').on('click', function () {
          $("#video1").attr("src", "");
        });
  
      }
    })();
   `;
    script.type = "text/javascript";
    script.async = "async";
    document.getElementsByTagName('header')[0].appendChild(script);
  }, []);
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
        <a href="/">
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
              <a href="/work">WORK</a>
            </li>
            <li id="02">
              <a href="/about">ABOUT</a>
              
            </li>
            <li id="03">
              <a href="/news">NEWS</a>
            </li>
            <li id="04">
              <a href="/contact">CONTACT</a>
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

        <a href="#." className="m_menu_close visible-xs">
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
    </header>
  );
};

export default Header;
