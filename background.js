// Open the side panel automatically when the user navigates to a LinkedIn profile.
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url && tab.url.includes("linkedin.com/in/")) {
    chrome.sidePanel.open({ tabId });
  }
});

// Listen for messages from the content script and forward them to the side panel.
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.profileData) {
    // Send the data to the side panel.
    chrome.runtime.sendMessage({ profileData: message.profileData });
    sendResponse({ status: "Data received by background script" });
  }
  return true; // Keep the message channel open for an async response.
});
