document.addEventListener("DOMContentLoaded", () => {
  playerName = document.getElementById("playerName").textContent.toLowerCase();
  fetch("/api/" + playerName).then(async (res) => (document.getElementById("score").innerText = await res.text()));
});
