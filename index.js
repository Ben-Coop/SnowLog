function updateDepth() {
    fetch('depth_log.txt?')
      .then(response => {
        if (!response.ok) {
          throw new Error("Network error");
        }
        return response.text();
      })
      .then(text => {
        const lines = text.trim().split('\n');
        const latestLines = lines.slice(0, 50);
        document.getElementById("depth").innerText = latestLines.join('\n');
      })
      .catch(error => console.error("Error fetching depth_log.txt:", error));
  }

  setInterval(updateDepth, 5000);
  window.onload = updateDepth;