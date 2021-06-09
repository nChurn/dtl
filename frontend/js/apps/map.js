var map = (function(){

  var init = function(){
    var width = $(document).width();
    ymaps.ready(function(){
      var lat = $('#map').data('lat') || 55.746715;
      var lng = $('#map').data('lng') || 37.536897;

      var map = new ymaps.Map("map", {
          center: [lat, lng],
          zoom: 17,
          controls: [],
      });
      map.behaviors
        .disable(['scrollZoom']);
      var placemark = new ymaps.Placemark([lat, lng], {}, {
          iconLayout: 'default#image',
          iconImageHref: document.getElementById('map').getAttribute('data-icon'),
          iconImageSize: [86, 108],
          iconImageOffset: [-35.5,-117]
      });
      map.geoObjects.add(placemark);
      var position = map.getGlobalPixelCenter();
      if (width >= 900) {
        map.setGlobalPixelCenter([ position[0] + 300, position[1] - 100]);
      }
      else if(width > 640 && width < 900){
        map.setGlobalPixelCenter([ position[0] + 250, position[1] + 0]);
      }
      else{
        map.setGlobalPixelCenter([ position[0] + 0, position[1] + 0]);
      }
    });
  };

  return {
    init : init
  };

})();
