var filters = (function(){

  var init = function(){
    mainFilters();
    selectFilter();
  };

  var directions = 'all';
  var industries = 'all';
  var main = 'all';

  var mainFilters = function(){
    $('.page_filter-title').each(function(index, element){
      var $el = $(element);
      $el.click(function(){
        $el.addClass('active').siblings().removeClass('active');
        main = $el.data('type');
        if($el.hasClass('js-project')){
          sendProjects(main, directions, industries);
        }
        else{
          $.ajax({
             type: "POST",
             url: '/filter_news/',
             data: { 'data' : main },
             success: function(response){
               if(response.error){
                 console.log('Oups!');
                 return false;
               }
               var content = $($.trim(response));
               $('.js-projects-items').html(content);
             },
             error: function(data){

             }
          });
        }
      });
    });
  };

  var selectFilter = function(){
    $('select.page_filter-select').each(function(index, element){
      var $el = $(element);
      $el.change(function(){
        if($el.hasClass('js-direct')){
          directions = $el.val();
          if(directions == 'all'){
            main = 'all';
          }
          if(directions == 'actives'){
            directions = 'all';
            main = 'active';
          }
          else{
            main = 'all';
          }
          $('.page_filter-select.js-industry').val('all').trigger('change');
        }
        if($el.hasClass('js-industry')){
          industries = $el.val();
        }
        sendProjects(main, directions, industries);
      });
    });
  };

  var sendProjects = function(main, directions, industries){
    var lang = $('.header').data('lang');
    $.ajax({
       type: "POST",
       url: '/filter_projects/',
       data: { 'data' : main, 'directions' : directions, 'industries' : industries, 'language': lang },
       success: function(response){
         if(response.error){
           console.log('Oups!');
           return false;
         }
         var content = $($.trim(response));
         $('.js-projects-items').html(content);
       },
       error: function(data){

       }
    });
  }

  return {
    init : init
  };

})();
