import React from 'react';

const Modal = () => {
    return (
        <div className="modal fade" id="work_detail_pop" role="dialog">
		<div className="modal-dialog modal-lg">
			<div className="modal-content pop_contents">
				<a href="#." data-dismiss="modal" className="modal_close_x"><i className="xi-close-thin"></i><span>닫기</span></a>
				<h4 className="text-center fs12 mb10 pt20"><span id="clientnm1"></span></h4>
				<h3 className="text-center"><span id="title1"></span></h3>		
				<div className="mt50 mt30-xs">
					<video src="" id="video1" width="100%" controls autoplay></video>
				</div>
				<a href="#." data-dismiss="modal" className="modal_close_x2"><i className="xi-close-thin"></i>팝업닫기</a>
			</div>
		</div>
	</div>
    )
}

export default Modal;