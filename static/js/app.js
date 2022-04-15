const copyrightYearRef = document.querySelector("#copyright-year");


  // Auto increment of the year in footer
  const getFullYear = () =>
    (copyrightYearRef.innerHTML = new Date().getFullYear());

  getFullYear(); 

  // Add slidedown animation to dropdown-menu
  $(".dropdown").on("show.bs.dropdown", function (e) {
    $(".dropdown-menu").removeClass("invisible");
    $(this).find(".dropdown-menu").first().stop(true, true).slideDown();
  });

  // Add slideup animation to dropdown-menu
  $(".dropdown").on("hide.bs.dropdown", function (e) {
    $(this).find(".dropdown-menu").first().stop(true, true).slideUp();
  });


  // Show the toast
  $(document).ready(function() {
    $(".toast").toast('show');
  });

