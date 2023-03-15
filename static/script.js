$('form').submit(function(event) {
  event.preventDefault();
  $('#send').addClass('disabled').find('.fas').removeClass('fa-paper-plane').addClass('fa-spinner fa-spin');
  socket.emit('message', $('#input').val());
  $('#input').val('');
});

socket.on('message', function(data) {
  $('#messages').append($('<p>').text(data)).scrollTop($('#messages')[0].scrollHeight);
  $('#send').removeClass('disabled').find('.fas').removeClass('fa-spinner fa-spin').addClass('fa-paper-plane');
});
