document.addEventListener("DOMContentLoaded", () => {
  // Create WebSocket connection.
  const socket = new WebSocket("/api/director");

  // Connection opened
  socket.addEventListener("open", (event) => {
    socket.send("Hello Server!");
  });

  // Listen for messages
  socket.addEventListener("message", (event) => {
    console.log(event);
  });
});
