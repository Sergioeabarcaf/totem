$( document ).ready(function() {
  var socket = io.connect();
  var alerta = document.getElementById('alerta');
  socket.on('new alerta', (data) => {
    alerta.innerText=data.value;
  });

});
