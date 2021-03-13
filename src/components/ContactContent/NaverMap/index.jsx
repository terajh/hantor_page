import React, { useState, useEffect } from 'react';

import { RenderAfterNavermapsLoaded, NaverMap, Marker } from 'react-naver-maps';


const NaverMapAPI = (props) => {
    const navermaps = window.naver.maps;
    const [[xLoc, yLoc], setstate] = useState([37.3595704, 127.105399])
    
    return (
        <NaverMap 
            id="map"
            mapDivID={'maps-getting-started-uncontrolled'}
            style={{
                width: '100%', // 네이버지도 가로 길이
                height: '100%'
            }}
            center={new navermaps.LatLng(xLoc, yLoc)}     // 지도 초기 위치
            defaultZoom={(xLoc === 37.3595704) ? 12 : 15}>   
            <Marker  position={new navermaps.LatLng(xLoc, yLoc)}
                animation={navermaps.Animation.BOUNCE}
                >
            </Marker>
        </NaverMap>
    )
}
const NaverMaps = (props) => {
    // eslint-disable-next-line

    return (
        <RenderAfterNavermapsLoaded
            ncpClientId={'fomot3guwd'} // 자신의 네이버 계정에서 발급받은 Client ID
            error={<p>Maps Load Error</p>}
            loading={<p>Maps Loading...</p>}
            >
            <NaverMapAPI ></NaverMapAPI>
        </RenderAfterNavermapsLoaded> 
    )
}

export default NaverMaps;