import React from "react";

const Footer = () => {
  return (
    <footer className="main_footer">
      <div className="container_outer clearfix text-center">
        {/* <ul className="list-unstyled clearfix mb0 dp-inblock">
						<li><a href="/">법적고지</a></li>
						<li><a href="/">이용약관</a></li>
						<li><a href="/" className="fw500 fcBlack">개인정보처리방침</a></li>
						<li><a href="https://www.doosan.com/kr/csr/csr-code/?menu=code-of-conduct" target="_blank">윤리경영</a></li>
						<li><a href="/">IR</a></li>
					</ul> */}
        <div className="copy eng">
          Copyright ⓒ 2021 by Hantor. All Rights Reserved.
          <br className="visible-xs" /> Hantor is a{" "}
          <span className="fcBlue">Ajou University</span>.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
