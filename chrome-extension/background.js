chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'ENRICH_PROFILE') {
      fetch('http://localhost:5000/enrich', {  // Your backend URL
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: message.url })
      })
      .then(response => response.json())
      .then(data => {
        chrome.storage.local.get({ history: [] }, result => {
          const history = result.history;
          history.push({ url: message.url, data });
          if (history.length > 5) history.shift();
          chrome.storage.local.set({ enrichedData: data, history });
          chrome.action.openPopup();
        });
      });
    }
  });