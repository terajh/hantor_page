import React from "react";
import LeftButton from "../LeftButton";
import ContainerOuter from "../ContainerOuter";
import './style.css'
const HomeMain = (props) => {
  return (
    <div id="main_contents" >
      <LeftButton></LeftButton>
      <ContainerOuter changeMode={props.changeMode}></ContainerOuter>
    </div>
  );
};

export default HomeMain;
