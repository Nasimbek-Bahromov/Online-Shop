(function ($) {
  "use strict";

  /*===========================================
        Table of contents
    01. Preloader
    02. Mobile Menu
    03. Sticky fix
    04. Scroll To Top
    05. Set Background Image
    06. One Page Nav Active
    =============================================*/


  /*---------- 01. Preloader ----------*/
  $(window).on('load', function () {
    $('.preloader').delay(100).fadeOut('slow');
  });

  


  /*---------- 03. Mobile Menu Active ----------*/
  $('.main-menu').vsmobilemenu({
    menuContainer: '.vs-mobile-menu',
    expandScreenWidth: 992,
  });


  /*---------- 03. Sticky fix ----------*/
  var lastScrollTop = '';
  function stickyMenu($targetMenu, $toggleClass) {
    var st = $(window).scrollTop();
    if ($(window).scrollTop() > 600) {
      if (st > lastScrollTop) {
        // hide sticky menu on scroll down
        $targetMenu.removeClass($toggleClass);

      } else {
        // active sticky menu on scroll up
        $targetMenu.addClass($toggleClass);
      };
    } else {
      $targetMenu.removeClass($toggleClass);
    };

    lastScrollTop = st;
  };
  // Scroll To top Button Select 
  var scrollToTopBtn = '.scrollToTop'
  $(window).on("scroll", function () {
    stickyMenu($('.sticky-header'), "active");

    //Check to see if the window is top if not then display button
    if ($(this).scrollTop() > 400) {
      $(scrollToTopBtn).addClass('show');
    } else {
      $(scrollToTopBtn).removeClass('show');
    }

  });



  /*---------- 04. Scroll To Top ----------*/
  $(scrollToTopBtn).on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    }, 4000);
    return false;
  });




  /*---------- 05.Set Background Image ----------*/
  if ($('.background-image').length > 0) {
    $('.background-image').each(function () {
      var src = $(this).attr('data-vs-img');
      $(this).css({
        'background-image': 'url(' + src + ')'
      });
    });
  };







  /*----------- 06. One Page Nav Active ----------*/
  function onePageNav() {
    $('.main-menu').find('a').each(function () {
      $(this).on('click', function (e) {
        e.preventDefault();
        var target = $(this.getAttribute('href'));
        if (target.length) {
          event.preventDefault();
          $('html, body').stop().animate({
            scrollTop: target.offset().top - 100
          }, 1000);
        };

      });
    });
  };
  onePageNav();






})(jQuery);