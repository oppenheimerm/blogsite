const menu_toggle = document.getElementById("mobile-menu-toggle");//.addEventListener('click', toggleSidenav,false);
const the_app = document.getElementById("app");


menu_toggle.addEventListener('click', () => {
    the_app.classList.toggle('is-active');
});





/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
/*function openNav() {
    document.getElementById("mobile-menu-toggle").style.width = "260px";
    document.getElementById("main").style.marginLeft = "260px";
  }
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
  /*function closeNav() {
    document.getElementById("app-sidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
  }*/