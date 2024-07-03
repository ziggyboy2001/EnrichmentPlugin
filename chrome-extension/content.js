if (window.location.href.includes('linkedin.com/in/')) {
    const enrichButton = document.createElement('button');
    enrichButton.textContent = 'Enrich Profile';
    enrichButton.style.position = 'fixed';
    enrichButton.style.top = '10px';
    enrichButton.style.right = '10px';
    enrichButton.style.zIndex = '1000';
    document.body.appendChild(enrichButton);
  
    enrichButton.addEventListener('click', () => {
      chrome.runtime.sendMessage({ type: 'ENRICH_PROFILE', url: window.location.href });
    });
  }