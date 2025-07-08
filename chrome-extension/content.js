(() => {
  const iframe = document.createElement("iframe");
  iframe.src = chrome.runtime.getURL("sidebar.html");
  iframe.style.cssText = `
    position: fixed;
    top: 0;
    right: 0;
    height: 100%;
    width: 380px;
    z-index: 999999;
    border: none;
    box-shadow: -2px 0 10px rgba(0,0,0,0.5);
    background: #212121;
    transition: transform 0.3s ease;
  `;
  document.body.appendChild(iframe);

  const videoId = new URLSearchParams(window.location.search).get("v");

  iframe.onload = () => {
    iframe.contentWindow.postMessage({ type: "VIDEO_ID", videoId }, "*");
  };
})();
