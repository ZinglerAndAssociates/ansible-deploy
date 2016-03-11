function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("hidden_ajax").innerHTML = xhttp.responseText;
    }
  };
  xhttp.open("GET", "manifest.json", true);
  xhttp.send();
}



// Shorthand for $( document ).ready()
$(function() {
    console.log( "minecraft.zinglax.com: READY" );

    loadDoc();
});


$("body").on("swipeleft",function(){
  var url = "#myPanel"
  window.location.replace(url);

});



// <!--Positions, (0=middle, 1=left, -1=right)-->
var pos = 0; 
(function()  {$(document).on("swipeleft",function(){
    if (pos == 0){
    document.getElementById("mypanel").click();
    }
    pos += 1
  });
})(); 
(function()  {$(document).on("swiperight",function(){
    // <!--alert("You swiped right!");-->
    if (pos == 0){
    document.getElementById("mypanel").click();
    }
    pos -= 1
  });
})(); 