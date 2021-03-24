 /* eslint-disable*/
import React, { useState, useEffect } from "react";
import { Route, BrowserRouter } from "react-router-dom";
import { Contact, Home, News, About, Work, Organization } from "../pages";
import { Header } from "../components";
import "../App.css";

const App = () => {
  const [mode, setMode] = useState("main");
  const toggleMode = (mod) => {
    setMode(mod);
  }
  const getContent = () => {
    if(mode === 'main') {
      return <Home></Home>;
    }else if(mode === 'contact') {
      return <Contact></Contact>;
    }else if(mode === 'about') {
      return <About></About>;
    }else if(mode === 'news') {
      return <News></News>;
    }else if(mode === 'work') {
      return <Work></Work>;
    }else if(mode === 'organization') {
      return <Organization></Organization>;
    }
  }
  return (
    <div id="wrap" className="main_wrap">
      <Header changeMode={toggleMode} mode={mode}></Header>
      {getContent()}
    </div>
  );
};

export default App;
/* eslint-enable*/