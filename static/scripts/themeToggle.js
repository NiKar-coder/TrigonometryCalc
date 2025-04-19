var dark = true;
var a = document.body;
var p = document.getElementById("themeToggler");

function darkLight() {
  dark = !dark;
  if (dark) {
    a.className = "theme-dark";
    p.innerHTML = "Light mode";
  } else {
    a.className = "theme-light";
    p.innerHTML = "Dark mode";
  }
  if (dark) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
}

window.addEventListener("DOMContentLoaded", (event) => {
  if (localStorage.getItem("theme") === "dark") {
    a.className = "theme-dark";
    p.innerHTML = "Light mode";
  } else {
    dark = false;
    a.className = "theme-light";
    p.innerHTML = "Dark mode";
  }
});
