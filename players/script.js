document.addEventListener("DOMContentLoaded", () => {
  playerName = document.getElementById("playerName").textContent.toLowerCase();
  fetch("/api/" + playerName).then(async (res) => (document.getElementById("score").innerText = await res.text()));

  document.getElementById("dec").addEventListener("click", () => {
    fetch("/api/" + playerName + "/minus", { method: "POST" }).then(async (res) => (document.getElementById("score").innerText = await res.text()));
  });
  document.getElementById("dec10").addEventListener("click", () => {
    fetch("/api/" + playerName + "/minusTen", { method: "POST" }).then(async (res) => (document.getElementById("score").innerText = await res.text()));
  });

  document.getElementById("inc").addEventListener("click", () => {
    fetch("/api/" + playerName + "/plus", { method: "POST" }).then(async (res) => (document.getElementById("score").innerText = await res.text()));
  });
  document.getElementById("inc10").addEventListener("click", () => {
    fetch("/api/" + playerName + "/plusTen", { method: "POST" }).then(async (res) => (document.getElementById("score").innerText = await res.text()));
  });
});
