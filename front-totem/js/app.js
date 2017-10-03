$(document).ready(function(){
	$(document).foundation();

	var lastScroll = 0;
	$(window).scroll(function(){
		var st = $(window).scrollTop();
		if ($('body').hasClass('admin-bar')) {
			if ((st > 10) && (st > lastScroll)) {
				$('.mobile-nav').css({top: 0});
				$('.menu-mobile-container').css({top: -42});
			} else {
				//arriba
				if (st < 45) {
					$('.mobile-nav').css({top: 45});
					$('.menu-mobile-container').css({top: 4});
				}
			}
		}
		lastScroll = st;
	});
	$('.mobile-nav-open').on('click',function(e) {
		e.preventDefault();
		$('.menu-mobile-container').toggleClass('hide');
		// if (!$('.menu-mobile-container').hasClass('hide')) {
		// 	var elem = new Foundation.Drilldown($('.menu-mobile-container').find('.vertical'), {
		// 		backButton : '<li class="js-drilldown-back"><a><span class="dashicons dashicons-arrow-left-alt"></span></a></li>'
		// 	});
		// }
		return false;
	});
	$('.menu-mobile-container').find('.close').on('click', function(e) {
		e.preventDefault();
		$(this).parent().addClass('hide');
		return false;
	});
});