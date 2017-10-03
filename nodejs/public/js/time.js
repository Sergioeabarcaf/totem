var hora = document.getElementById('hora');
var fecha = document.getElementById('fecha');
var meses = new Array ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre");
var dias = new Array ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo");
var horaActual = "";
var fechaActual = "";

function updateTime(){
  var time = new Date();
  horaActual = time.getHours() + " : " + time.getMinutes() + " hrs.";
  hora.innerText = horaActual;
  fechaActual = time.getDate() + " de " + meses[time.getMonth()] + " de " + time.getFullYear();
  fecha.innerText = fechaActual;
  setTimeout("updateTime()",10000);
}
