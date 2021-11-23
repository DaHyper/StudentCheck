function toggleDivClass(id) {
  let hidden = document.getElementById(id).classList.contains("hidden");
  if (hidden) {
    document.getElementById(id).classList.remove("hidden");
  } else {
    document.getElementById(id).classList.add("hidden");
  }
}

let important = document.getElementsByClassName("updated-name");
for (let i = 0; i < important.length; i++) {
  document.getElementById("notification-list").innerHTML += "<hr>" + important[i].textContent;
}

// chaning themes

const lightButton = document.getElementById("light-btn");
const darkButton = document.getElementById("dark-btn");

const theme = localStorage.getItem("theme");
if (theme) {
  document.body.classList.add(theme);
  if (theme == "dark") {
    document.documentElement.style.cssText = `
    --accent: var(--dark-accent); 
    --top: var(--dark-top);
    --card: var(--dark-card);
    `;
  }
} else {
  document.body.classList.add("light");
  document.documentElement.style.cssText = `
  --accent: var(--light-accent);
  --top: var(--light-top);
  `;
}

lightButton.onclick = () => {
  document.body.classList.replace("dark", "light");
  localStorage.setItem("theme", "light");
  // document.documentElement.style.cssText = `
  // --accent: var(--light-accent);
  // --top: var(--light-top);
  // `;

}
darkButton.onclick = () => {
  document.body.classList.replace("light", "dark");
  localStorage.setItem("theme", "dark");
  document.documentElement.style.cssText = `
  --accent: var(--dark-accent);
  --top: var(--dark-top);
  --card: var(--dark-card);
  `;
}

