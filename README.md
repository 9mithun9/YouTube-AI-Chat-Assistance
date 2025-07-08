
# 🎥 YouTube AI Assistant Extension

A Chrome extension that injects a smart AI sidebar into YouTube videos. It extracts the video ID and allows you to interact with an AI backend (via FastAPI) to summarize or answer questions about the video.

---

## ✨ Features

- Sidebar injected into YouTube video pages
- Extracts the current video ID automatically
- Sends video ID to FastAPI backend
- Displays transcript-based AI answers
- Simple, responsive sidebar UI
- Built with vanilla JS, Chrome Extension API, and Python FastAPI

---

## 🧠 How It Works

1. `content.js` injects a sidebar (`sidebar.html`) into YouTube pages
2. It parses the `videoId` from the current URL
3. Once the iframe loads, the `videoId` is passed via `postMessage()`
4. The sidebar frontend sends this to a FastAPI server (`localhost:8000`)
5. AI processes transcript and returns intelligent responses

---

## 🧩 Chrome Extension Setup

### 1. Load Unpacked Extension

1. Open `chrome://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select the `chrome-extension/` folder

### 2. Files in Extension

```
chrome-extension/
├── content.js
├── sidebar.html
├── sidebar.js
├── style.css
├── background.js
├── manifest.json
```

---

## 🧪 Backend Setup (FastAPI)

### 1. Setup Python Environment

```bash
cd backend/
python -m venv venv
source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 2. Start the Server

```bash
uvicorn app:app --reload
```

This should run on: `http://localhost:8000`

---

## 🔑 Notes

- `.env` file must **never** be committed. Make sure `.env` and your API keys are in `.gitignore`.
- Chrome extension needs `host_permissions` for `http://localhost:8000/` to access your backend.

---

## 📦 Manifest Overview

```json
"content_scripts": [{
  "matches": ["*://www.youtube.com/watch*"],
  "js": ["content.js"]
}],
"web_accessible_resources": [{
  "resources": ["sidebar.html", "style.css", "sidebar.js"],
  "matches": ["<all_urls>"]
}]
```

---

## 📷 Screenshot

*Add a screenshot of the sidebar inside a YouTube page here*

---

## 📄 License

MIT License
