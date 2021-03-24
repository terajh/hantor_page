
function main_ui_js(){
	var swiper = new Swiper('.swiper-container', {
		direction: 'horizontal',
		slidesPerView: 3,
		spaceBetween: 0,
		//mousewheelControl: true,
		speed: 900,
		loop: true,
		pagination: '.swiper-pagination',
		paginationType: 'fraction',
		nextButton: '.control-next',
		prevButton: '.control-prev',
		 breakpoints: {
			992: {
			  slidesPerView: 2,
			},
		 }
	});
}

$('body').on('mousewheel DOMMouseScroll', function(e){
  if(typeof e.originalEvent.detail == 'number' && e.originalEvent.detail !== 0) {
	if(e.originalEvent.detail > 0) {
		$('.control-next').trigger('click');
	} else if(e.originalEvent.detail < 0){
		$('.control-prev').trigger('click');
	}
  } else if (typeof e.originalEvent.wheelDelta == 'number') {
	if(e.originalEvent.wheelDelta < 0) {
		$('.control-next').trigger('click');
	} else if(e.originalEvent.wheelDelta > 0) {
		$('.control-prev').trigger('click');
	}
  }
});


$(function(){
	$('.mobile_work_list .view_type1').on('click' , function(){
		$('.view_type2').removeClass('active');
		$(this).addClass('active');
		$('.m_list_type').removeClass('type2');
	});
	$('.mobile_work_list .view_type2').on('click' , function(){
		$('.view_type1').removeClass('active');
		$(this).addClass('active');
		$('.m_list_type').addClass('type2');
	});

	$('.mobile_menu_btn').on('click',function(){
		$('header').addClass('m_menu_open');
		var item = $('<div class="menu_blind"></div>').hide();
		$('header').append(item);
		item.fadeIn();
	});
	$('.m_menu_close').on('click',function(){
		$('header').removeClass('m_menu_open');
		$('.menu_blind').fadeOut().remove();
	});
	$(document).on('click', '.menu_blind', function(){
		$('header').removeClass('m_menu_open');
		$('.menu_blind').fadeOut().remove();
	});
});

$(function () {
    var $setElem = $('.switchImg'),
		pcName = '-pc',
		moName = '-mo',
		mobileWidth = 992;
    $setElem.each(function () {
        var $this = $(this);
 
        function imgSize() {
            if (window.innerWidth > mobileWidth) {
                $this.attr('src', $this.attr('src').replace(moName, pcName)).css({
                    visibility: 'visible'
                });
            } else {
                $this.attr('src', $this.attr('src').replace(pcName, moName)).css({
                    visibility: 'visible'
                });
            }
        }
        $(window).resize(function () {
            imgSize();
        });
        imgSize();
    });

});


$(function(){
	AOS.init();
	var wh = $("#wrap").height();
	
	setTimeout(function(){
		var winh = $(window).height();
		console.log('wrap' + wh);
		console.log('window' + winh);
		if(wh < winh){
			$('.sub_footer').addClass('sf_fixed');
		}
	},100);
})

$(document).ready(function(){
	main_ui_js();
});