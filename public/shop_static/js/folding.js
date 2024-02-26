$(function() {
    $("tbody tr:not(.parent)").hide();
    $(".parent").click(function() {
      $(this).toggleClass("selected");
      $("tbody tr:not(.parent)").hide();
      if ($(this).hasClass("selected")) {
        $(this).nextUntil(".parent").show();
      } else {
        $(this).nextUntil(".parent").hide();
      }
    });
  })