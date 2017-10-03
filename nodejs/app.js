var express = require('express'),
	app = express(),
	server = require('http').createServer(app),
	io = require("socket.io").listen(server),
	nicknames = {},
	mqtt = require('mqtt'),
	//client = mqtt.connect('mqtt://192.168.150.2:1883'),
	client = mqtt.connect('mqtt://192.168.1.134:1883'),
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
	client.subscribe('alerta')
});

//generar el schema para cargar a la db
client.on('message', function(topic, message) {
	if(topic=="alerta"){
		io.sockets.emit('new alerta', message.toString());
	}
	else{
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
			}
		})

		//Condicional para ejecutar la funcion correspondiente a cada dashboard
		if(topic=="temperatura"){
			io.sockets.emit('new temperatura', {
				value: splitMessage[1].toString()
			});
		}

		if(topic=="humedad"){
			io.sockets.emit('new humedad', {
				value: splitMessage[1].toString()
			});
		}

		if(topic=="presion"){
			io.sockets.emit('new presion', {
				value: splitMessage[1].toString()
			});;
		}

		if(topic=="uv"){
			io.sockets.emit('new uv', {
				value: splitMessage[1].toString()
			});
		}
	}
});


//Puerto donde corre el sistema
server.listen(80);

//Ruteo a las paginas
app.use(express.static(__dirname + '/public'));
app.get('/', function(req, res) {
	res.sendFile(__dirname + '/views/index.html');
});
app.get('/flora-fauna',function(req,res){
	res.sendFile(__dirname + '/views/flora-fauna.html');
});
app.get('/informacion-general',function(req,res){
	res.sendFile(__dirname + '/views/informacion-general.html');
});
app.get('/normas-del-parque',function(req,res){
	res.sendFile(__dirname + '/views/normas-del-parque.html');
});
app.get('/rutas',function(req,res){
	res.sendFile(__dirname + '/views/rutas.html');
});
app.get('/chat', function(req, res) {
	res.redirect('http://192.168.252.250/chat');
});
