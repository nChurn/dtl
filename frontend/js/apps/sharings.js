$(window).ready(function () {
  (function (w) {
    function createWindow(url) {
      var width = 800;
      var height = 500;
      var top = Math.round(screen.height / 3 - height / 2);
      var left = Math.round(screen.width / 2 - width / 2);
      return window.open(url, '', 'left=' + left + ',top=' + top + ',width=' + width + ',height=' + height + ',personalbar=0,toolbar=0,scrollbars=1,resizable=1');
    }

    function share(network, share) {
      var defaultValues = { url: '', title: '', image: '', text: '' };
      var _extend = $.extend(defaultValues, share);

      var url = _extend.url;
      var title = _extend.title;
      var image = _extend.image;
      var text = _extend.text;

      url = encodeURIComponent(url);

      createWindow({
        ok: 'https://odnoklassniki.ru/dk?st.cmd=addShare&st.s=1&st.comments=' + text + '&st._surl=' + url,
        vk: 'https://vk.com/share.php?url=' + url + '&title=' + title + '&image=' + image + '&description=' + text,
        tw: 'https://twitter.com/intent/tweet?url=' + url + '&text=' + text,
        fb: 'https://www.facebook.com/sharer/sharer.php?u=' + url
      }[network]);
    }

    w.share = share;


    $('.socials_item').click(function(e){
      e.stopPropagation();
      var data = $(this).data('sharing');
      var id = $(this).data('id');

      share(data, {
        url: 'http://' + window.location.hostname + '/news/' + id
      });

    });
  }(window));
});
