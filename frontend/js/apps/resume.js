var resume = (function(){

  var file;

  var init = function(){
    drag();
    sendForm();
  };

  var sendForm = function(){
    $('#form_resume').submit(function(e){
      e.preventDefault();
      $('.submit_button').attr('disabled', true);
      ajaxData = new FormData($(this)[0]);
      if($(this).find('input.error').length){
        $('.submit_button').attr('disabled', false);
        $('.popup_form-error').show();
        return false;
      }
      else{
        $('.popup_form-error').hide();
      }
      ajaxData.set('type', $(this).data('type'));
      if(file){
        ajaxData.set('file', file);
      }

      $.ajax({
         type: "POST",
         url: '/send_resume/',
         data: ajaxData,
         cache: false,
         contentType: false,
         enctype: 'multipart/form-data',
         processData: false,
         success: function(data){
           if(data.result == 'ok'){
             $('.form_ok').trigger('click');
             $('.form-popup .js-close').trigger('click');
           }
         },
         error: function(data){
           alert('Упс. Что-то пошло не так.');
         }
      });
    });
  }

  var drag = function(){
    var $block = $('.popup_input-file');

    $block.change(function(e){
      var filename = $block.val().split('\\').pop();
      $('.popup_result .popup_file-title').text(filename);
      $(this).removeClass('draged').addClass('loaded');
    });

    $block.on('dragenter', function (e){
      e.preventDefault();
      $(this).addClass('draged');
    });

    $block.on('dragleave', function (e){
      e.preventDefault();
      $(this).removeClass('draged');
    });

    $block.on('dragover', function (e){
      e.preventDefault();
    });

    $block.on('drop dragdrop', function (e){
      e.preventDefault();
      $(this).removeClass('draged').addClass('loaded');
      var resume = e.originalEvent.dataTransfer.files;
      file = resume[0];
      $('.popup_result .popup_file-title').text(resume[0].name);
    });

    $('.popup_file-reset').click(function(){
      file = '';
      $block.removeClass('draged loaded');
      $('.popup_result .popup_file-title').text('');
    });
  }

  return {
    init : init
  };

})();
