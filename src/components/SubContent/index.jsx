import React from "react";
import "./style.css";

const SubContent = () => {
  return (
    <div id="sub_contents">
      <div className=" sub0201_wrap">
        <div className="sec01 pl15-xs">
          <div className="container">
            <h3 className="mb20 mb10-xs">
              <div
                id="rev-2"
                className="dp-inblock mask_title block-revealer"
              >
                <div id="content_title" className="block-revealer__content">
                  "HANTOR"
                </div>
                <div
                  className="block-revealer__element"
                ></div>
              </div>
            </h3>
            <h4 data-aos="fade-left" data-aos-delay="1400">
            '누구나 쓸 수 있도록 열려 있는 넓은 터'
            </h4>
          </div>
          <div className="box_area" data-aos="fade-left" data-aos-delay="1600">
            <div className="container_outer">
              <div className="container">
                <div className="box fw300">
                  
                  학교를 다니는 4년동안, 처음 심은 씨앗이 열매를 맺을 수 있도록
                  위에서 끌고 아래서 쫓아가는 소프트웨어학과의
                  대표적인 학술 소학회로 자리매김하였습니다.
                </div>
              </div>
            </div>
          </div>
        </div>

        <div
          className="sec02 pl15-xs"
          data-aos="fade-left"
          data-aos-delay="1800"
        >
          <div className="container">
            <h3 className="sub_title2 mb20">Since 1989</h3>
            <div className="row">
              <div className="col-sm-6 fw300 mb40-xs">
                본 학과 최대 규모이자, 2019년 기준 31년의 최고 역사를 자랑하는
                <br />
                학술 소학회 <span className="fw400">HANTOR</span>는 매년 활동 재학생 학우 수 약 150명을 자랑하는
                <br />
                명실상부한 소프트웨어학과의 가장 큰 소학회입니다.
                <br />
              </div>
              <div className="col-sm-6 fw300">
                소학회 회원들끼리 머리를 모아 보다 전문적인 지식을 쌓아 
                <br className="hidden-sm" />
                <span className="fw400">
                  SW
                </span>
                가 중요시되는 세계 트렌드에서 중요한 역할을 수행하는 
                <br className="hidden-sm" />
                IT인재로서 성장하고자 합니다.
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </div>
  );
};
export default SubContent;
