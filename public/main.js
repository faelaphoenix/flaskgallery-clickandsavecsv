// ----- custom js ----- //
 
$(function() {
 
  // sanity check
  console.log( "ready!" );
 
  // image click
  $("#img").click(function() {
 
    // add active class to clicked picture
    $(this).addClass("active")
 
    // grab image url
    var image = $(this).attr("src")
    console.log(image)
 
  });
 
});