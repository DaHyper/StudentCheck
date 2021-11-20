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
  document.getElementById("notification-list").innerHTML += "<hr>" + important[i].textContent
}
