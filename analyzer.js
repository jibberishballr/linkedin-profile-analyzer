document.addEventListener('DOMContentLoaded', function() {
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    console.log("Received message in analyzer:", request);
    if (request.profileData) {
      updateAnalyzerUI(request.profileData);
    }
  });
});

function updateAnalyzerUI(data) {
  if (data.connection_probability) {
    const score = Math.round(data.connection_probability * 100);
    document.getElementById('connection-score').textContent = `${score}%`;
  }
  if (data.contact_info) {
    document.getElementById('contact-info').textContent = data.contact_info.email || 'Not found';
  }
  // Placeholder for engagement analytics
  document.getElementById('engagement-analytics').textContent = 'Coming soon...';
}
