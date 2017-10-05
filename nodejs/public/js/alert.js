$( document ).ready(function() {
  var socket = io.connect();
  var alerta = document.getElementById('alerta');

  console.log("ejecutado");
  socket.on('new alerta', (data) => {
    alerta.innerText=data.value;
  });

});
