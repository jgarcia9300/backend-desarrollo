/* Created by Tivotal */

document.addEventListener("DOMContentLoaded", () => {
  let sideMenu = document.querySelectorAll(".nav-link");
  sideMenu.forEach((item) => {
    let li = item.parentElement;

    item.addEventListener("click", () => {
      sideMenu.forEach((link) => {
        link.parentElement.classList.remove("active");
      });
      li.classList.add("active");
    });
  });

  let menuBar = document.querySelector(".menu-btn");
  let sideBar = document.querySelector(".sidebar");
  menuBar.addEventListener("click", () => {
    sideBar.classList.toggle("hide");
  });

  let switchMode = document.getElementById("switch-mode");
  switchMode.addEventListener("change", (e) => {
    if (e.target.checked) {
      document.body.classList.add("dark");
      localStorage.setItem("dark-mode", "true");
    } else {
      document.body.classList.remove("dark");
      localStorage.setItem("dark-mode", "false");
    }
    applyDarkModeToIframes(e.target.checked);
  });

  // Apply dark mode based on stored preference
  if (localStorage.getItem("dark-mode") === "true") {
    document.body.classList.add("dark");
    switchMode.checked = true;
    applyDarkModeToIframes(true);
  }

  let searchFrom = document.querySelector(".content nav form");
  let searchBtn = document.querySelector(".search-btn");
  let searchIcon = document.querySelector(".search-icon");
  searchBtn.addEventListener("click", (e) => {
    if (window.innerWidth < 576) {
      e.preventDefault();
      searchFrom.classList.toggle("show");
      if (searchFrom.classList.contains("show")) {
        searchIcon.classList.replace("fa-search", "fa-times");
      } else {
        searchIcon.classList.replace("fa-times", "fa-search");
      }
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 576) {
      searchIcon.classList.replace("fa-times", "fa-search");
      searchFrom.classList.remove("show");
    }
    if (window.innerWidth < 768) {
      sideBar.classList.add("hide");
    }
  });

  if (window.innerWidth < 768) {
    sideBar.classList.add("hide");
  }

  function applyDarkModeToIframes(isDark) {
    const iframes = document.querySelectorAll("iframe");
    iframes.forEach((iframe) => {
      iframe.contentWindow.postMessage({
        type: "toggle-dark-mode",
        dark: isDark
      }, "*");
    });
  }
});
