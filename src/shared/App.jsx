import React from "react";
import { Route, BrowserRouter } from "react-router-dom";
import { Contact, Home, News, About, Work, Organization } from "../pages";
import "../App.css";
const App = () =>{
    return (
      <BrowserRouter basename={process.env.PUBLIC_URL}>
        <Route exact path="/" component={Home}></Route>
        <Route path="/Contact" component={Contact}></Route>
        <Route path="/About" component={About}></Route>
        <Route path="/News" component={News}></Route>
        <Route path="/Organization" component={Organization}></Route>
        <Route path="/Work" component={Work}></Route>
      </BrowserRouter>
    );
  
}

export default App;
