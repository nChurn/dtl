var popups = (function(){

  var self = {};

  var init = function(){
    self.triggers = $('.js-trigger');
    self.popups = $('.js-popup');
    self.body = $('html, body');
    self.bodyStyle = {};
    self.scrollTop = 0;
    self.ios = !!navigator.platform && /iPad|iPhone|iPod/.test(navigator.platform);

    initTriggers();
  };

  var popupShow = function(popup){
    popup.fadeIn(500);
    if((device.mobile() || device.tablet()) && self.ios){
      self.bodyStyle = document.body.style;
      self.scrollTop = {
          obj : document.documentElement.scrollTop === 0 ? document.body : document.documentElement,
          scrollTop: document.documentElement.scrollTop === 0 ? document.body.scrollTop : document.documentElement.scrollTop,
      }
      popup.css('position', 'absolute');
      document.body.style.overflow = 'hidden';
      document.body.style.height = '100%';
      document.body.style.width = '100%';
      document.body.style.position = 'fixed';
    }
    else{
      self.body.addClass('-opened-popup');
    }
  };

  var popupClose = function(popup){
    popup.fadeOut(300);
    if((device.mobile() || device.tablet()) && self.ios){
        document.body.style=self.bodyStyle;
        self.scrollTop.obj.scrollTop = self.scrollTop.scrollTop;
    }
    if($('.form-popup').length){
      var $form = $('#form_resume');
      $form[0].reset();
      $('.submit_button').attr('disabled', false);
      $form.find('.popup_input-file').removeClass('draged loaded');
      $form.find('input').removeClass('error');
      $('.popup_form-error').hide();
    }
    self.body.removeClass('-opened-popup');
  };

  var initTriggers = function(){
    self.triggers.each(function(index, element){
      var $el = $(element);
      $el.click(function(){
        var data = $el.data('popup');

        var popup  = self.popups.filter(function(){
          return $(this).data('popup') == data;
        });

        popupShow(popup);
        popup.find('.js-close').click(function(e){
          popupClose(popup);
        });

        popup.find('.js-content').click(function(e){
          e.stopPropagation();
          return;
        });

        if(data == 'form'){
          popup.find('form').data('type', $el.data('type'));
        }
      });
    });
  };

  return {
    init : init
  };

})();
