import React from 'react';
import {Footer, HomeMain} from '../../components';


const Home = (props) => {
    return (
        <>
            <HomeMain changeMode={props.changeMode}></HomeMain>
            <Footer></Footer>
        </>
    )
}

export default Home;