let videoId = null;

window.addEventListener("message", (event) => {
  if (event.data?.type === "VIDEO_ID") {
    videoId = event.data.videoId;
  }
});

const askBtn = document.getElementById("askBtn");
const clearBtn = document.getElementById("clearBtn");
const status = document.getElementById("status");
const answerBox = document.getElementById("answer");

askBtn.addEventListener("click", async () => {
  const question = document.getElementById("question").value.trim();
  if (!question) return;

  if (!videoId) {
    answerBox.textContent = "Could not get video ID.";
    answerBox.classList.remove("collapsed");
    return;
  }

  status.innerHTML = `<span class="spinner"></span>Typing...`;
  answerBox.classList.add("collapsed");

  try {
    const res = await fetch("http://localhost:8000/ask-question", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ video_id: videoId, question }),
    });

    const data = await res.json();
    answerBox.textContent = data.answer || "No answer returned";
    answerBox.classList.remove("collapsed");

    answerBox.scrollTop = answerBox.scrollHeight;
  } catch (err) {
    answerBox.textContent = "Server error.";
    answerBox.classList.remove("collapsed");
  }

  status.textContent = "";
});

clearBtn.addEventListener("click", () => {
  document.getElementById("question").value = "";
  answerBox.textContent = "";
  status.textContent = "";
  answerBox.classList.add("collapsed");
});
