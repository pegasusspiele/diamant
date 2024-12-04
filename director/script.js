document.addEventListener("DOMContentLoaded", () => {
  container = document.getElementById("container");

  const socket = new WebSocket("/api/state");

  let state = undefined;

  socket.addEventListener("open", (event) => {});

  socket.addEventListener("message", (event) => {
    console.log("received state from server", JSON.parse(event.data));
    state = JSON.parse(event.data);

    for (const key of Object.keys(state)) {
      console.log(key, state[key]);

      document.getElementById("score_" + key).innerText = state[key];
    }
  });

  document.getElementById("resetButton").addEventListener("click", () => {
    fetch("/api/reset", { method: "GET" });
  });
});
