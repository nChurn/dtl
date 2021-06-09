$(document).ready(function() {
  $('.page_filter-select').styler({
    selectSmartPositioning: false
  });
  $('.popup_form').validate({
    errorPlacement: function(error,element) {
      return true;
    }
  });

  $('.preloader').fadeOut();

  (function(){
    var $form = $('.language');
    var $input = $form.find('input.js-lang');

    $('.js-change-lang').click(function(){
      if($(this).hasClass('-active')) return false;
      var lang = $(this).data('lang');
      $input.val(lang);
      $form.submit();
    });
  })();

  resume.init();
  popups.init();
  filters.init();
  search.init();

  if($('.index').length){
    if(!detectIE()){
      $('.index_headline-logo').addClass('not-ie');
    }
    else{
      $('.index_headline').addClass('ie');
    }
  }

  if(detectIE()){
    $('.page_content').addClass('ie');
  }

  if(device.mobile() || device.tablet()){

  }
  else{
    animations.init();
  }



  var $header = $('.header');

  $(document).mousewheel(function(event) {
    if(event.deltaY > 0){
      $header.addClass('showed');
      if(!$header.hasClass('fixed')){
        $header.removeClass('-light');
        if(!$('.js-header-show').hasClass('added')){
          $header.addClass('-index');
        }
      }
    }
    if(event.deltaY < 0){
      if($header.hasClass('fixed')){
        setTimeout(function(){
            $header.removeClass('showed');
        }, 500);
      }
    }
  });

  var headerWaypoint = new Waypoint({
    element: $('.js-header-show'),
    handler: function(direction) {
      if(direction == 'down'){
        $header.addClass('fixed');
        $header.removeClass('index-animated animated showed');
      }
      if(direction == 'up'){
        $header.removeClass('fixed -light');
      }
    },
    offset: 60
  })

  $('.js-waypoint').each(function(index, element){
    var $el = $(element);
    var waypoint = new Waypoint({
      element: $el,
      handler: function(direction) {
        if(direction == 'down'){
          if($el.hasClass('lights')){
            $header.addClass('-light');
            $header.removeClass('-index');
          }
          if($el.hasClass('darks')){
            $header.removeClass('-light');
            $header.removeClass('-index');

          }
          if($el.hasClass('main')){
            $header.removeClass('-light');
          }
        }
        if(direction == 'up'){
          if(!$el.hasClass('lights')){
            $header.addClass('-light');
            $header.removeClass('-index');
          }
          if(!$el.hasClass('darks')){
            $header.removeClass('-light');
            $header.removeClass('-index');
          }
          if($el.hasClass('main')){
            $header.removeClass('-light');
            $header.addClass('-index');
          }
        }
      },
      offset: 135
    })
  });


});
