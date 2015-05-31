$(document).ready(function(){
	$('#about').click(function(event){
		event.preventDefault()
		console.log('click')
		$('.modal').show();
		$('.insert').show();
		$('body').addClass('modal-open');
	})
	$('.insert').click(function(e){
		if ($('body').hasClass('modal-open')){
			if (! $('.modal').is(e.target) && $('.modal').has(e.target).length ===0){
				$('.insert').hide();
				$('.modal').hide();
				$('body').removeClass('modal-open');
			}
		}
	})
	fartscroll(300);
})