var socket = io.connect();
var alerta = document.getElementById('alerta');

socket.on('new alerta', (data) => {
  console.log(data);
  alerta.innerText=data;
});
