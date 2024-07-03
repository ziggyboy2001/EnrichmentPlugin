function showTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(tab => {
      tab.style.display = 'none';
    });
    document.getElementById(tabId).style.display = 'block';
  }
  
  chrome.storage.local.get('enrichedData', data => {
    document.getElementById('tab1').textContent = JSON.stringify(data.enrichedData.tab1, null, 2);
    document.getElementById('tab2').textContent = JSON.stringify(data.enrichedData.tab2, null, 2);
    document.getElementById('tab3').textContent = JSON.stringify(data.enrichedData.tab3, null, 2);
  });
  
  showTab('tab1');