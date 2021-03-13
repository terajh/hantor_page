import React from 'react';

const SubScript = () => {
    return (
        <>
        <script id="rendered-js" >
		jQuery(function ($) {
			function history_slide(){
				var $frame = $('#basic');
				var $slidee = $frame.children('ul').eq(0);
				var $wrap = $frame.parent();

				// Call Sly on frame
				$frame.sly({
				  horizontal: 1,
				  itemNav: 'basic',
				  activateMiddle: 1,
				  smart: 1,
				  activateOn: 'click',
				  mouseDragging: 1,
				  touchDragging: 1,
				  releaseSwing: 1,
				  startAt: 0,
				  scrollBar: $wrap.find('.scrollbar'),
				  scrollBy: 1,
				  pagesBar: $wrap.find('.pages'),
				  activatePageOn: 'click',
				  speed: 300,
				  elasticBounds: 1,
				  easing: 'easeOutExpo',
				  dragHandle: 1,
				  dynamicHandle: 1,
				  clickBar: 1,

				  // Buttons
				  forward: $wrap.find('.forward'),
				  backward: $wrap.find('.backward'),
				  prev: $wrap.find('.prev'),
				  next: $wrap.find('.next'),
				  prevPage: $wrap.find('.prevPage'),
				  nextPage: $wrap.find('.nextPage') });
			}
			history_slide();
			$(window).resize(function(){
				history_slide();
			});
		});
		
    </script>
	<script type="text/javascript">
		(function() {
		// Fake loading.
		setTimeout(init, 1000);
		function init() {
			document.body.classList.remove('loading');
			var rev1 = new RevealFx(document.querySelector('#rev-1'), {
				revealSettings : {
					bgcolor: '#000000',
					onCover: function(contentEl, revealerEl) {
						contentEl.style.opacity = 1;
					}
				}
			});
			rev1.reveal();

			var rev2 = new RevealFx(document.querySelector('#rev-2'), {
				revealSettings : {
					bgcolor: '#ef5025',
					delay: 250,
					onCover: function(contentEl, revealerEl) {
						contentEl.style.opacity = 1;
					}
				}
			});
			rev2.reveal();

			
		}
	})();
	</script>
    </>
    )
}