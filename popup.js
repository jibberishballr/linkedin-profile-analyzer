document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('subscribe').addEventListener('click', function() {
    var email = document.getElementById('email').value;
    if (email) {
      chrome.runtime.sendMessage({email: email}, function(response) {
        console.log(response);
      });
    }
  });
});
