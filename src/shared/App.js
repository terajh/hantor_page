import React, {Component} from 'react'
import {Route} from 'react-router-dom';
import {Contact, Home, News, About, Work, Organization} from '../pages';
import '../App.css'
class App extends Component {
  render() {
    return (
      <div id="wrap" className="main_wrap">
        <Route exact path="/" component={Home}></Route>
        <Route path="/Contact" component={Contact}></Route>
        <Route path="/About" component={About}></Route>
        <Route path="/News" component={News}></Route>
        <Route path="/Organization" component={Organization}></Route>
        <Route path="/Work" component={Work}></Route>
      </div>
    )
  }
}

export default App;
