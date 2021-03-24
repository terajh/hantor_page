import React from "react";
import "./style.css";
import logo from "../../assets/comm/logo.png";
import { Swiper, SwiperSlide } from "swiper/react";
import SwiperCore, { Navigation, Pagination, Scrollbar, A11y } from "swiper";
import {ArrayGet} from '../index'
// Import Swiper styles
import "swiper/swiper.scss";
import "swiper/components/navigation/navigation.scss";
import "swiper/components/pagination/pagination.scss";
import "swiper/components/scrollbar/scrollbar.scss";
import Fade from 'react-reveal/Fade';

// Import Swiper styles
SwiperCore.use([Navigation, Pagination, Scrollbar, A11y]); // *

const ContainerOuter = (props) => {
  const getContent = () => {
    return  ArrayGet.map((el, index) => (
      <SwiperSlide 
        data-target="#work_detail_pop"
        data-title={el.title}
        data-clientnm={el.client}
        data-idx="183"
        data-toggle="modal"
        key={index}>
        <a href='#' id={el.id} key={index}>
          <div className="txt_con">
            <div>
              <p className="eng s_title">{el.title}</p>
              <p className="title">{el.client}</p>
              <p className="more"></p>
            </div>
          </div>
        </a>
      </SwiperSlide>
    ));
  }

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
          <Fade left>
            <div id="rev-1" className="content__title__inner">
              <img
                src={logo}
                className="wp100"
                style={{ maxWidth: 519 + "px" }}
                alt="hantor"
              />
            </div>
          </Fade>
        </h1>

        <p className="more_about" data-aos="fade-right" data-aos-delay="1000">
          <a href="#" onClick={()=> {
            props.changeMode('work');
          }}>
            More Work <i className="animate03"></i>
          </a>
        </p>

        <div className="main_fp_scroll hidden-xs">
          Scroll <img src="/assets/carousel4.jpg" width="33px" alt="" />
          <span></span>
        </div>

        <Swiper
          className='swiper-container'
          navigation
          scrollbar={{ draggable: true }}
          pagination={{ clickable: true }}
          slidesPerView={3}
          spaceBetween={0}
          onSlideChange={() => console.log("slide change")}
        >
          {getContent()}
        </Swiper>
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
          <a href="#">
            ABOUT US <i className="animate03"></i>
          </a>
        </p>
      </section>
    </div>
  );
};

export default ContainerOuter;
