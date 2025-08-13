document.addEventListener('DOMContentLoaded', function() {
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.profileData) {
      updateAnalyzerUI(request.profileData);
    }
  });
});

function updateAnalyzerUI(data) {
  // For now, we'll just display the raw data.
  // In the future, this will be parsed and displayed in the correct sections.
  document.getElementById('connection-score').textContent = JSON.stringify(data, null, 2);
}
