import React from "react";

const WorkContent = () => {
  return (
    <div id="sub_contents" style={{paddingBottom: 0+'px'}}>
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
            data-aos="fade-zoom-in"
            data-aos-delay="200"
            data-aos-duration="500"
            data-target="#work_detail_pop"
            data-file="ikaria_long(2).mp4"
            data-title="이카리아 : 죽음을 잊은 자"
            data-clientnm="동아오츠카"
            data-idx="183"
            data-toggle="modal"
          >
            {" "}
            <a
              onClick="showMovie('이카리아 : 죽음을 잊은 자','동아오츠카','ikaria_long(2).mp4')"
            >
              {" "}
              <div className="txt_con">
                {" "}
                <div>
                  {" "}
                  <p className="eng s_title">동아오츠카</p>{" "}
                  <p className="title">이카리아 : 죽음을 잊은 자</p>{" "}
                  <p className="more"></p>{" "}
                </div>{" "}
              </div>{" "}
            </a>{" "}
          </div>
          </div>
        <div className="more more_list" >
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
