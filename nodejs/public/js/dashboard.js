$( document ).ready(function() {
  var socket = io.connect();
  var presion = document.getElementById('presion');
  var humedad = document.getElementById('humedad');
  var radiacion = document.getElementById('radiacion');

//Funciones que actualizan los valores del dashboard
  //actualiza valor dashboard temperatura
  socket.on('new temperatura', (data) => {
    temperatura.innerText=data.value;
    console.log(data.time);
    console.log("temperatura");
  });
  //actualiza valor dashboard humedad
  socket.on('new humedad', (data) => {
    humedad.innerText=data.value;
    console.log(data.time);
    console.log("humedad");
  });
  //actualiza valor dashboard presion
  socket.on('new presion', (data) => {
    presion.innerText=data.value;
    console.log(data.time);
    console.log("presion");
  });
  //actualiza valor dashboard UV
  socket.on('new uv', (data) => {
    radiacion.innerText=data.value;
    console.log(data.time);
    console.log("uv");
  });
});
