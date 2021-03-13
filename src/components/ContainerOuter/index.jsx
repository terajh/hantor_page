import React from "react";
import './style.css'
const ContainerOuter = () => {
  return (
    <div className="container_outer">
      <section id="main_work_list">
        <h1
          className="logo"
          data-aos="fade-zoom-in"
          data-aos-easing="ease-in-back"
          data-aos-delay="800"
          data-aos-offset="0"
        >
          <div id="rev-1" className="content__title__inner">
            <img
              src="/web/img/comm/logo.png"
              className="wp100"
              style={{maxWidth: 519+"px"}}
              alt="hantor"
            />
          </div>
        </h1>

        <p className="more_about" data-aos="fade-right" data-aos-delay="1000">
          <a href="/Work">
            More Work <i className="animate03"></i>
          </a>
        </p>

        <div className="main_fp_scroll hidden-xs">
          Scroll{" "}
          <img
            src="/web/img/icon/more_arrow_w.png"
            width="33px"
            alt=""
          />
          <span></span>
        </div>

        <div className="swiper-container hidden-xs">
          <div className="swiper-wrapper">
            <div
              className="swiper-slide"
              data-target="#work_detail_pop"
              data-title="이카리아 : 죽음을 잊은 자"
              data-clientnm="동아오츠카"
              data-idx="183"
              data-toggle="modal"
            >
              <a id="aka">
                <div className="txt_con">
                  <div>
                    <p className="eng s_title">동아오츠카</p>
                    <p className="title">이카리아 : 죽음을 잊은 자</p>
                    <p className="more"></p>
                  </div>
                </div>
              </a>
            </div>
          </div>
        </div>
        <div
          className="main_work_control"
          data-aos="fade-left"
          data-aos-delay="1000"
        >
          <div className="swiper-pagination eng"></div>
          <div className="dp-inblock clearfix">
            <div className="control-prev eng">PREV</div>
            <p className="pull-left">/</p>
            <div className="control-next eng">NEXT</div>
          </div>
        </div>
        <div className="mobile_work_list visible-xs">
          <div className="list_view_type text-right pr30 mb10">
            <a href="#." className="view_type1 active">
              <span></span>하나씩보기
            </a>
            <a href="#." className="view_type2">
              <span></span>두개씩 보기
            </a>
          </div>
          <ul className="list-unstyled clearfix m_list_type"></ul>
        </div>
        <p className="more_about more_work text-center pt40 visible-xs">
          <a href="/about">
            ABOUT US <i className="animate03"></i>
          </a>
        </p>
      </section>
    </div>
  );
};

export default ContainerOuter;
