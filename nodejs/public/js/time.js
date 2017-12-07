var hora = document.getElementById('hora');
var fecha = document.getElementById('fecha');
var meses = new Array ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre");
var dias = new Array ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo");

function updateTime(){
  time = new Date();
  if(time.getMinutes()<10){
    horaActual = time.getHours() + ":0" + time.getMinutes() + " hrs.";
  }
  else {
    horaActual = time.getHours() + ":" + time.getMinutes() + " hrs.";
  }
  hora.innerText = horaActual;
  delete horaActual;
  fechaActual = time.getDate() + " de " + meses[time.getMonth()] + " de " + time.getFullYear();
  fecha.innerText = fechaActual;
  delete fechaActual;
  delete time;
  setTimeout("updateTime()",10000);
}
