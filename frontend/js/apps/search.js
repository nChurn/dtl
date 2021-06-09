var search = (function(){

  var init = function(){
    var $icon = $('.page_filters_search-icon');
    var $input = $('.page_filters_search-input');

    $icon.click(function(e){
      e.stopPropagation();
      $icon.addClass('opened');
      $input.fadeIn().focus();
    });

    $input.blur(function(){
      $input.fadeOut().val('');
      $icon.removeClass('opened');
    });

    $input.parent('form').submit(function(e){
      e.preventDefault();
      var val = $input.val();
      if($input.hasClass('js-news')){
        var type = 'news';
      }
      else{
        var type = 'projects';
      }
      if(val){
        window.location.href = '/search?type='+ type +'&search=' + val;
      }
      else{
        $input.trigger('blur');
      }
    });
  };

  return {
    init : init
  };

})();
