import React from "react";
import "./style.css";
import Flip from "react-reveal/Flip";
import { ArrayGet } from "../index";

const WorkContent = () => {
  const getContent = () => {
    return ArrayGet.map((el, index) => (
      <Flip left>
        <div
          className="grid-item aos-init aos-animate"
          data-target="#work_detail_pop"
          data-title={el.title}
          data-clientnm={el.client}
          data-idx="183"
          data-toggle="modal"
          key={index}
        >
          {" "}
          <a id={el.id}>
            {" "}
            <div className="txt_con">
              {" "}
              <div>
                {" "}
                <p className="eng s_title">{el.title}</p>{" "}
                <p className="title">{el.client}</p> <p className="more"></p>{" "}
              </div>{" "}
            </div>{" "}
          </a>{" "}
        </div>
      </Flip>
    ));
  };

  return (
    <div id="sub_contents" style={{ paddingBottom: 0 + "px" }}>
      <div className="list_view_type  pl10 mb20 visible-xs">
        <a href="#." className="view_type1 active">
          <span></span>하나씩보기
        </a>
        <a href="#." className="view_type2">
          <span></span>두개씩 보기
        </a>
      </div>

      <div className="container_outer sub0101_wrap pageon">
        <div className="grid clearfix">{getContent()}</div>
        <div className="more more_list">
          <a href="#.">
            <span>더보기</span>
            <i className="xi-angle-down-thin"></i>
          </a>
        </div>
      </div>

      <div className="modal fade" id="work_detail_pop" role="dialog">
        <div className="modal-dialog modal-lg">
          <div className="modal-content pop_contents">
            <a href="#." data-dismiss="modal" className="modal_close_x">
              <i className="xi-close-thin"></i>
              <span>닫기</span>
            </a>
            <h4 className="text-center fs12 mb10 pt20">
              <span id="clientnm1"></span>
            </h4>
            <h3 className="text-center">
              <span id="title1"></span>
            </h3>
            <div className="mt50 mt30-xs">
              <video
                src=""
                id="video1"
                width="100%"
                controls=""
                autoPlay=""
              ></video>
            </div>
            <a href="#." data-dismiss="modal" className="modal_close_x2">
              <i className="xi-close-thin"></i>팝업닫기
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WorkContent;
