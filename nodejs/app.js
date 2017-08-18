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
	client.subscribe('lumens');
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
	splitMessage = message.toString().split("/");
	//Schema sensores
	var sensor = new Sensor({
		paramSensor: String(topic),
		dato: String(splitMessage[1]),
		idTotem: String(splitMessage[0]),
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
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new temperatura");
	}

	if(topic=="humedad"){
		io.sockets.emit('new humedad', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new humedad");
	}

	if(topic=="presion"){
		io.sockets.emit('new presion', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new presion");
	}

	if(topic=="puntoRocio"){
		io.sockets.emit('new puntoRocio', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new puntoRocio");
	}

	if(topic=="viend_ins_grado"){
		io.sockets.emit('new viend_ins_grado', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new viend_ins_grado");
	}

	if(topic=="vel_2m"){
		io.sockets.emit('new vel_2m', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new vel_2m");
	}

	if(topic=="lluvia_1h"){
		io.sockets.emit('new lluvia_1h', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new lluvia_1h");
	}

	if(topic=="uv"){
		io.sockets.emit('new uv', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new uv");
	}

	if(topic=="lummens"){
		io.sockets.emit('new lummens', {
			value: String(splitMessage[1])
		});
		console.log("Emitio el mensaje a new lummens");
	}
});

//Puerto donde corre el sistema
server.listen(80);

//Ruteo a las paginas
app.use(express.static(__dirname + '/public'));
app.get('/', function(req, res) {
	res.sendFile(__dirname + '/views/index.html');
});
app.get('/chat', function(req, res) {
	res.redirect('http://192.168.252.250/views/chat');
});
app.get('/dashboard',function(req,res){
	res.sendFile(__dirname + '/views/dashboard.html');
});

//Abre conexion con socket
io.sockets.on('connection', function(socket) {
	//Funciones para actualizar los parametros del dashboard
	socket.on('send temperatura', function(data) {
		console.log(data);
		io.sockets.emit('new temperatura', {
			value: data
		});
	});

	socket.on('send humedad', function(data) {
		console.log(data);
		io.sockets.emit('new humedad', {
			value: data
		});
	});

	socket.on('send presion', function(data) {
		console.log(data);
		io.sockets.emit('new presion', {
			value: data
		});
	});

	socket.on('send puntoRocio', function(data) {
		console.log(data);
		io.sockets.emit('new puntoRocio', {
			value: data
		});
	});

	socket.on('send viend_ins_grado', function(data) {
		console.log(data);
		io.sockets.emit('new viend_ins_grado', {
			value: data
		});250
	});

	socket.on('send vel_2m', function(data) {
		console.log(data);
		io.sockets.emit('new vel_2m', {
			value: data
		});
	});

	socket.on('send lluvia_1h', function(data) {
		console.log(data);
		io.sockets.emit('new lluvia_1h', {
			value: data
		});
	});

	socket.on('send uv', function(data) {
		console.log(data);
		io.sockets.emit('new uv', {
			value: data
		});
	});

	socket.on('send lummens', function(data) {
		console.log(data);
		io.sockets.emit('new lummens', {
			value: data
		});
	});

});
