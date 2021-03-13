import React from "react";
import NaverMap from "./NaverMap";
import './style.css';

const Contacts = () => {
  return (
    <div id="sub_contents">
      <div className=" sub0401_wrap">
        <div className="container_outer relative">
          <div className="container">
            
            <h3 className="sub_title2 fcOrange pb30 pl20-xs">
              <div
                id="rev-2"
                className="dp-inblock mask_title block-revealer"
              >
                <div className="block-revealer__content">
                  Office.
                </div>
                <div
                  className="block-revealer__element"
                ></div>
              </div>
            </h3>
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
                    <span>대표전화</span>
                    02.519.6900
                  </li>
                  <li data-aos="fade-up" data-aos-delay="1700">
                    <i className="xi-print"></i>
                    <span>팩스번호</span>
                    02.519.6999
                  </li>
                  <li data-aos="fade-up" data-aos-delay="1900">
                    <i className="xi-mail"></i>
                    <span>이메일</span>
                    hancomm@hancomm.co.kr
                  </li>
                </ul>
              </div>
              <div className="col-md-6">
                <ul className="list-unstyled">
                  <li data-aos="fade-up" data-aos-delay="1500">
                    <i className="xi-library-video"></i>
                    <span>광고대행 / 제작 문의</span>
                    02.519.6916
                  </li>
                  <li data-aos="fade-up" data-aos-delay="1700">
                    <i className="xi-desktop"></i>
                    <span>전시 / 이벤트 / 출판 문의</span>
                    02.519.6946
                  </li>
                  <li data-aos="fade-up" data-aos-delay="1900">
                    <i className="xi-video-call"></i>
                    <span>미디어 문의</span>
                    02.519.6969
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div
          className="pt80 mt20 pt20-xs"
          data-aos="fade-up"
          data-aos-delay="2100"
          style={{height:500+'px'}}
        >
          <NaverMap></NaverMap>
        </div>
      </div>
    </div>
  );
};

export default Contacts;
