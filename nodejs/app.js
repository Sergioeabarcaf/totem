var express = require('express'),
	app = express(),
	server = require('http').createServer(app),
	io = require("socket.io").listen(server),
	nicknames = {},
	mqtt = require('mqtt'),
	client = mqtt.connect('mqtt://192.168.150.2:1883'),
	Sensor = require("./models/sensor").Sensor,
	document = require("min-document");

//subscribe a los topicos de los sensores
client.on('connect', function() {
	client.subscribe('temperatura');
	client.subscribe('humedad');
	client.subscribe('puntoRocio');
	client.subscribe('presion');
	client.subscribe('altitud');
	client.subscribe('presion_nivelMar');
	client.subscribe('temperatura_BMP');
	client.subscribe('lummens');
	client.subscribe('uv');
	client.subscribe('viend_ins_grado');
	client.subscribe('viend_chr');
	client.subscribe('viend_2m_grados');
	client.subscribe('vel_2m');
	client.subscribe('raf_ins');
	client.subscribe('raf_10m');
	client.subscribe('raf_ins_grados');
	client.subscribe('raf_10m_grados');
	client.subscribe('lluvia_1h');
	client.subscribe('lluvia_24h');
});

//generar el schema para cargar a la db
client.on('message', function(topic, message) {
	//Schema sensores
	var sensor = new Sensor({
		paramSensor: String(topic),
		dato: message,
		fechaYHora: Date()
	});

	//Guardar en la db los datos.
	sensor.save(function(err) {
		if (err) {
			console.log(err);
		} else {
			console.log("los datos fueron cargados a la db " + sensor.paramSensor);
		}
	})

	//Condicional para ejecutar la funcion correspondiente a cada dashboard
	if(topic=="temperatura"){
		io.sockets.emit('new temperatura', {
			value: dato
		});
		console.log("Emitio el mensaje a new temperatura");
	}

	if(topic=="humedad"){
		io.sockets.emit('new humedad', {
			value: dato
		});
		console.log("Emitio el mensaje a new humedad");
	}

	if(topic=="presion"){
		io.sockets.emit('new presion', {
			value: dato
		});
		console.log("Emitio el mensaje a new presion");
	}

	if(topic=="uv"){
		io.sockets.emit('new uv', {
			value: dato
		});
		console.log("Emitio el mensaje a new uv");
	}
});

//Puerto donde corre el sistema
server.listen(80);

//Ruteo a las paginas
app.use(express.static(__dirname + '/public'));
app.get('/', function(req, res) {
	res.sendFile(__dirname + '/views/index.html');
});
app.get('/dashboard',function(req,res){
	res.sendFile(__dirname + '/views/dashboard.html');
});
app.get('/chat', function(req, res) {
	res.redirect('192.168.250.2/chat');
});
