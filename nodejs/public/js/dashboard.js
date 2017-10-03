$( document ).ready(function() {
  var socket = io.connect();
  var presion = document.getElementById('presion');
  var humedad = document.getElementById('humedad');
  var radiacion = document.getElementById('radiacion');

//Funciones que actualizan los valores del dashboard
  //actualiza valor dashboard temperatura
  socket.on('new temperatura', function(data) {
    console.log("temperatura: "+ data);
    temperatura.innerText=data;
  });
  //actualiza valor dashboard humedad
  socket.on('new humedad', function(data) {
    console.log("humedad: "+ data);
    humedad.innerText=data;
  });
  //actualiza valor dashboard presion
  socket.on('new presion', function(data) {
    console.log("presion: "+ data);
    presion.innerText=data;
  });
  //actualiza valor dashboard UV
  socket.on('new uv', function(data) {
    console.log("radiacion: "+ data);
    radiacion.innerText=data;
  });
});
