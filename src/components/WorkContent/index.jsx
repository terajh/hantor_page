import React from "react";
import './style.css'
const WorkContent = () => {
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
        <div className="grid clearfix">
          <div
            className="grid-item aos-init aos-animate"
            data-target="#work_detail_pop"
            data-title="한터 가입신청"
            data-clientnm="너와 나의 만남"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a id="aka4" href="#">
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">한터 가입신청</p>{" "}
                  <p className="title">너와 나의 만남</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
          <div
            className="grid-item aos-init aos-animate"
            data-target="#work_detail_pop"
            data-title="벚꽃 사진전"
            data-clientnm="너와, 기억"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a id="aka2">
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">벚꽃 사진전</p>{" "}
                  <p className="title">너와, 기억</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
          <div
            className="grid-item aos-init aos-animate"
            data-target="#work_detail_pop"
            data-title="아주인의 날"
            data-clientnm="너와, 행사"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a id="aka3">
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">아주인의 날</p>{" "}
                  <p className="title">너와, 행사</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
          <div
            className="grid-item aos-init aos-animate"
            data-target="#work_detail_pop"
            data-title="스터디"
            data-clientnm="너와, 발전"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a id="aka1">
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">스터디</p>{" "}
                  <p className="title">너와, 발전</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
          <div
            className="grid-item aos-init aos-animate"
            data-target="#work_detail_pop"
            data-title="봄 MT"
            data-clientnm="너와, 추억"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a id="aka6">
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">봄 MT</p>{" "}
                  <p className="title">너와, 추억</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
          <div
            className="grid-item aos-init aos-animate"
            data-target="#work_detail_pop"
            data-title="OB & YB"
            data-clientnm="너와, 경험"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a id="aka5">
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">OB & YB</p>{" "}
                  <p className="title">너와, 경험</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
        </div>
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
