$( document ).ready(function() {
  var socket = io.connect();

//Dashboard de temperatura
  var temperatura = new LinearGauge({
    renderTo: 'temperatura',
    width: 150,
    height: 300,
    units: "°C",
    minValue: -20,
    startAngle: 90,
    ticksAngle: 180,
    valueBox: false,
    maxValue: 50,
    majorTicks: [
        "-20",
        "-10",
        "0",
        "10",
        "20",
        "30",
        "40",
        "50"
    ],
    minorTicks: 10,
    strokeTicks: false,
    colorPlate: "#fff",
    borderShadowWidth: 0,
    borders: false,
    needleType: "arrow",
    needleWidth: 2,
    needleCircleSize: 7,
    needleCircleOuter: true,
    needleCircleInner: false,
    colorNeedle: "#fb0000",
    colorBarProgress: "#fb0000",
    animationDuration: 1500,
    animationRule: "linear",
    barWidth: 10,
    value: 0,
    valueBox: "true"
  }).draw();

//dashboard de humedad
  var humedad = new LinearGauge({
    renderTo: 'humedad',
    width: 150,
    height: 300,
    units: "%",
    minValue: 0,
    startAngle: 90,
    ticksAngle: 180,
    valueBox: false,
    maxValue: 100,
    majorTicks: [
        "0",
        "20",
        "40",
        "60",
        "80",
        "100"
    ],
    minorTicks: 1,
    strokeTicks: false,
    colorPlate: "#fff",
    borderShadowWidth: 0,
    borders: false,
    needleType: "arrow",
    needleWidth: 2,
    needleCircleSize: 7,
    needleCircleOuter: true,
    needleCircleInner: false,
    colorNeedle: "rgba(0, 0, 255, 0.6)",
    colorBarProgress: "rgba(0, 0, 255, 0.6)",
    animationDuration: 1500,
    animationRule: "linear",
    barWidth: 10,
    value: 0,
    valueBox: "true"
  }).draw();

//dashboard de UV
  var uv = new LinearGauge({
    renderTo: 'uv',
    width: 150,
    height: 300,
    units: "Indice UV",
    minValue: 0,
    startAngle: 90,
    ticksAngle: 180,
    valueBox: false,
    maxValue: 12,
    majorTicks: [
        "0",
        "2",
        "4",
        "6",
        "8",
        "10",
        "11+"
    ],
    highlights: [
            {
                "from": 0,
                "to": 3,
                "color": "rgba(0, 255, 0, 1)"
            },
            {
                "from": 3,
                "to": 6,
                "color": "rgba(255, 255, 1, 1)"
            },
            {
                "from": 6,
                "to": 8,
                "color": "rgba(255, 99, 1, 1)"
            },
            {
                "from": 8,
                "to": 11,
                "color": "rgba(255, 0, 0, 1)"
            },
            {
                "from":11 ,
                "to": 12,
                "color": "rgba(139, 0, 255, 1)"
            }

    ],
    minorTicks: 1,
    strokeTicks: false,
    colorPlate: "#fff",
    borderShadowWidth: 0,
    borders: false,
    needleType: "arrow",
    needleWidth: 2,
    needleCircleSize: 7,
    needleCircleOuter: true,
    needleCircleInner: false,
    colorNeedle: "rgba(0, 255, 0, 0.6)",
    animationDuration: 1500,
    animationRule: "linear",
    barWidth: 10,
    value: 0,
    valueBox: "true"
  }).draw();

//dashboard de presion
  var presion = new RadialGauge({
    renderTo: 'presion',
    width: 250,
    height: 250,
    units: "hPa",
    minValue: 200,
    maxValue: 1200,
    majorTicks: [
        "200",
        "400",
        "600",
        "800",
        "1000",
        "1200"
    ],
    minorTicks: 2,
    strokeTicks: true,
    highlights: [
        {
            "from": 1000,
            "to": 1200,
            "color": "rgba(200, 50, 50, .75)"
        }
    ],
    colorPlate: "#fff",
    borderShadowWidth: 0,
    borders: false,
    needleType: "arrow",
    needleWidth: 2,
    needleCircleSize: 7,
    needleCircleOuter: true,
    needleCircleInner: false,
    animationDuration: 1500,
    animationRule: "linear"
  }).draw();


//Funciones que actualizan los valores del dashboard
  //actualiza valor dashboard temperatura
  socket.on('new temperatura', function(data) {
    console.log("Entro a new temperatura");
    temperatura.value = parseFloat(data.value);
    console.log(parseFloat(data.value));
  });
  //actualiza valor dashboard humedad
  socket.on('new humedad', function(data) {
    console.log("Entro a new humedad");
    humedad.value = parseFloat(data.value);
    console.log(parseFloat(data.value));
  });
  //actualiza valor dashboard presion
  socket.on('new presion', function(data) {
    console.log("Entro a new presion");
    presion.value = parseFloat(data.value);
    console.log(parseFloat(data.value));
  });
  //actualiza valor dashboard UV
  socket.on('new uv', function(data) {
    console.log("Entro a new uv");
    uv.value = parseFloat(data.value);
    console.log(parseFloat(data.value));
  });
});
