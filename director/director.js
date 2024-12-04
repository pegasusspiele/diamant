var container = null;

function renderState(state) {
  console.log(container);
}

document.addEventListener("DOMContentLoaded", () => {
  container = document.getElementByID("container")
  const socket = new WebSocket("/api/director");
  socket.addEventListener("open", (event) => {});
  socket.addEventListener("message", (event) => {
    renderState(JSON.parse(event.data));
  });
});
