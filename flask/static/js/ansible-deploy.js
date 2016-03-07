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
