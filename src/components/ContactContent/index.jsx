import React from "react";
import NaverMap from "./NaverMap";
import "./style.css";
import Fade from "react-reveal/Fade";

const Contacts = () => {
  return (
    <div id="sub_contents">
      <div className=" sub0401_wrap">
        <div className="container_outer relative">
          <div className="container">
            <h3 className="sub_title2 fcOrange pb30 pl20-xs">
              <div id="rev-2" className="dp-inblock mask_title block-revealer">
                <div id="content_title2" className="block-revealer__content">
                  Office.
                </div>
                <div className="block-revealer__element"></div>
              </div>
            </h3>
            <Fade left cascade>
              <p
                className="addr  pl20-xs"
                data-aos="fade-left"
                data-aos-delay="1200"
              >
                서울시 강남구 언주로 726 두산빌딩 3층, 5층
              </p>
              <hr className="visible-xs visible-sm mt40 mb40" />
              <div className="row cs_info pt80 pt0-sm">
                <div className="col-md-6 mb40-sm">
                  <ul className="list-unstyled">
                    <li data-aos="fade-up" data-aos-delay="1500">
                      <i className="xi-call"></i>
                      <span>대표 전화</span>
                      000.0000.0000
                    </li>
                    <li data-aos="fade-up" data-aos-delay="1700">
                      <i className="xi-print"></i>
                      <span>팩스번호</span>
                      02.519.6999
                    </li>
                    <li data-aos="fade-up" data-aos-delay="1900">
                      <i className="xi-mail"></i>
                      <span>이메일</span>
                      hantor@hantor.co.kr
                    </li>
                  </ul>
                </div>
                <div className="col-md-6">
                  <ul className="list-unstyled">
                    <li data-aos="fade-up" data-aos-delay="1500">
                      <a
                        href="https://www.facebook.com/AjouHantor"
                        className="fa fa-facebook"
                      ></a>
                      <span>페이스북</span>
                      <br></br>
                    </li>
                    <li data-aos="fade-up" data-aos-delay="1700">
                      <a href="#" className="fa fa-instagram"></a>
                      <span>인스타그램</span>
                      <br></br>
                    </li>
                    <li data-aos="fade-up" data-aos-delay="1900">
                      <i className="xi-video-call"></i>
                      <span>미디어 문의</span>
                      <br></br>
                    </li>
                  </ul>
                </div>
              </div>
            </Fade>
          </div>
        </div>

        <div
          className="pt80 mt20 pt20-xs"
          data-aos="fade-up"
          data-aos-delay="2100"
          style={{ height: 500 + "px" }}
        >
          <NaverMap></NaverMap>
        </div>
      </div>
    </div>
  );
};

export default Contacts;
