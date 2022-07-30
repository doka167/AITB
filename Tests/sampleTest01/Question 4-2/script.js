function darkMode() {
    var element = document.body;
    var navig = document.getElementById("navmode");
    element.className = "dark-mode";
    navig.className =  "dark-nav";

  
}
function lightMode() {
    var element = document.body;
    var navig = document.getElementById("navmode");
    element.className = "light-mode";
    navig.className =  null;
}