var animations = (function(){

  var init = function(){

    if($('.index').length){
      indexAnimations();
    }
    else{
      $('.header').addClass('animated');
      pageAnimations();
    }

    if($('.js-light').length){
      $('.header').addClass('-index');
    }

    $('.page').addClass('animated');

    var screenHeight = $(window).height();

    $('.js-fade').each(function(index, element){
      var $el = $(element);
      var waypoint = new Waypoint({
        element: $el,
        handler: function(direction) {
          $el.addClass('faded');
        },
        offset: screenHeight - 150
      })
    });

    var waypointBg = new Waypoint({
      element: $('.page_content'),
      handler: function(direction) {
        if(direction == 'down'){
          $('.page_headline-bg').css('position', 'absolute');
        }
        if(direction == 'up'){
          $('.page_headline-bg').css('position', 'fixed');
        }
      },
      offset: 0
    })
  };

  var pageAnimations = function(){
    if(!detectIE()){
      var parallaxPageBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration:  '200%'}});
      new ScrollMagic.Scene({triggerElement: ".js-parallax"})
        .setTween(".js-parallax div", {y: 0, ease: Linear.easeNone})
        .addTo(parallaxPageBg);
    }

    var parallaxLetters = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration:  '200%'}});
    new ScrollMagic.Scene({triggerElement: ".page_bg-text"})
      .setTween(".page_bg-text", {y: 100, ease: Linear.easeNone})
      .addTo(parallaxLetters);

    var controllerBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration: "100%"}});
    new ScrollMagic.Scene({triggerElement: ".page_content.opacity"})
      .setTween(".page_content.opacity", {backgroundColor: 'rgba(255,255,255,1)', ease: Linear.easeNone})
      .addTo(controllerBg);
  };

  var indexAnimations = function(){
    $('.index_headline').addClass('animated');
    $('.header').addClass('index-animated');

    if(!detectIE()){
      var controllerMainBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration: "100%"}});
      new ScrollMagic.Scene({triggerElement: ".index_info"})
        .setTween(".index_headline-bg", {alpha: 0, ease: Linear.easeNone})
        .addTo(controllerMainBg);

      var controllerMainLogo = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration: "100%"}});
      new ScrollMagic.Scene({triggerElement: ".index_info"})
        .setTween(".index_headline-content-wrapper", {alpha: 0, y: -400, ease: Linear.easeNone})
        .addTo(controllerMainBg);
    }

    var controllerInfoBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onLeave", duration: "100%"}});
    new ScrollMagic.Scene({triggerElement: ".index_headline"})
      .setTween(".index_info-bg", {alpha: 1, ease: Linear.easeNone})
      .addTo(controllerMainBg);

    var controllerProjectsBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration: $('.index_projects').innerHeight()}});
    new ScrollMagic.Scene({triggerElement: ".index_projects"})
      .setTween(".index_projects-bg", {left: "-95%", ease: Linear.easeNone})
      .addTo(controllerProjectsBg);

    var parallaxTeamBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration:  $('.index_team').innerHeight() * 2}});
    new ScrollMagic.Scene({triggerElement: ".index_team"})
      .setTween(".index_team-bg", {y: 300, ease: Linear.easeNone})
      .addTo(parallaxTeamBg);

    var parallaxMapBg = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration:  $('.index_map').innerHeight() + 200}});
    new ScrollMagic.Scene({triggerElement: ".index_map"})
      .setTween(".index_map-bg", {y: 50, ease: Linear.easeNone})
      .addTo(parallaxMapBg);
  };

  return {
    init : init
  };

})();
