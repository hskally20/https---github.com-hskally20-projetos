(function($) {
  "use strict"; // Start of use strict

  // Toggle the sidebar navigation
  $("#sidebarToggle").on('click', function(e) {
      $("body").toggleClass("sidebar-toggled");
      $(".sidebar").toggleClass("toggled");

      if ($(".sidebar").hasClass("toggled")) {
          $('.sidebar .collapse').collapse('hide'); // Hide any expanded menus
      }
  });

  // Hide menus and toggle sidebar when window is resized
  $(window).resize(function() {
      if ($(window).width() < 768) {
          $('.sidebar .collapse').collapse('hide');
      }

      // Automatically collapse sidebar on screens smaller than 480px
      if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
          $("body").addClass("sidebar-toggled");
          $(".sidebar").addClass("toggled");
          $('.sidebar .collapse').collapse('hide');
      }
  });

  // Prevent content scrolling when the fixed sidebar is scrolled over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
      if ($(window).width() > 768) {
          var e0 = e.originalEvent,
              delta = e0.wheelDelta || -e0.detail;
          this.scrollTop += (delta < 0 ? 1 : -1) * 30; // Adjust scroll speed
          e.preventDefault();
      }
  });

  // Show/hide "scroll-to-top" button based on scroll position
  $(document).on('scroll', function() {
      var scrollDistance = $(this).scrollTop();
      if (scrollDistance > 100) {
          $('.scroll-to-top').fadeIn();
      } else {
          $('.scroll-to-top').fadeOut();
      }
  });

  // Smooth scrolling for "scroll-to-top" button
  $(document).on('click', 'a.scroll-to-top', function(e) {
      var $anchor = $(this);
      $('html, body').stop().animate({
          scrollTop: ($($anchor.attr('href')).offset().top)
      }, 1000, 'easeInOutExpo');
      e.preventDefault();
  });

})(jQuery); // End of use strict
