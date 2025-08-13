chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.email) {
      console.log("Email received:", request.email);
      // Here you would typically send the email to your server
      sendResponse({status: "Email received"});
    }
  }
);
