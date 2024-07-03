chrome.storage.local.get('history', result => {
    const historyList = document.getElementById('history-list');
    result.history.forEach(entry => {
      const li = document.createElement('li');
      li.textContent = `${entry.url}: ${JSON.stringify(entry.data)}`;
      historyList.appendChild(li);
    });
  });