const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// fade out bootstrap alerts jQuery
setTimeout(function () {
  $('#message').fadeOut('slow');
}, 3000);