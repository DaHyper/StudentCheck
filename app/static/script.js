function toggleDivClass(id) {
  let hidden = document.getElementById(id).classList.contains("hidden");
  if (hidden) {
    document.getElementById(id).classList.remove("hidden");
  } else {
    document.getElementById(id).classList.add("hidden");
  }
}

// getting notifications
let important = document.getElementsByClassName("updated-name");
for (let i = 0; i < important.length; i++) {
  document.getElementById("notification-list").innerHTML += "<hr>" + important[i].textContent;
}

// changing themes

const themeButton = document.getElementById("theme-btn")

let theme = localStorage.getItem("theme");
if (theme) {
  document.body.classList.add(theme);
  document.getElementById("theme-btn").classList.add("btn-" + theme);
} else {
  document.body.classList.add("light");
  document.getElementById("theme-btn").classList.add("btn-light");

}

themeButton.onclick = () => {
  if (theme === "light") {
    
    themeButton.classList.replace("btn-light", "btn-dark");
    document.body.classList.replace("light", "dark");
    localStorage.setItem("theme", "dark");
  } else {
    themeButton.classList.replace("btn-dark", "btn-light");
    document.body.classList.replace("dark", "light");
    localStorage.setItem("theme", "light");
  }
  theme = localStorage.getItem("theme");
 }
