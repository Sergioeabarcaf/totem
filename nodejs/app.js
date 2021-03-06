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
	client.subscribe('presion');
	client.subscribe('uv');
	client.subscribe('alerta')
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
			}
		})

		//Condicional para ejecutar la funcion correspondiente a cada dashboard
		if(topic=="alerta"){
			io.sockets.emit('new alerta', {
				value: splitMessage[1].toString(),
				time: Date()
			});
		}

		if(topic=="temperatura"){
			io.sockets.emit('new temperatura', {
				value: splitMessage[1].toString(),
				time: Date()
			});
		}

		if(topic=="humedad"){
			io.sockets.emit('new humedad', {
				value: splitMessage[1].toString(),
				time: Date()
			});
		}

		if(topic=="presion"){
			io.sockets.emit('new presion', {
				value: splitMessage[1].toString(),
				time: Date()
			});;
		}

		if(topic=="uv"){
			io.sockets.emit('new uv', {
				value: splitMessage[1].toString(),
				time: Date()
			});
		}
});


//Puerto donde corre el sistema
server.listen(80);

//Ruteo a index
app.use(express.static(__dirname + '/public'));
app.get('/', function(req, res) {
	setTimeout(function(){
		Sensor.findOne({paramSensor: "alerta"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new alerta', {
					value: sensor.dato.toString(),
					time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	setTimeout(function(){
		Sensor.findOne({paramSensor: "temperatura"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new temperatura', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	setTimeout(function(){
		Sensor.findOne({paramSensor: "humedad"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new humedad', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	setTimeout(function(){
		Sensor.findOne({paramSensor: "presion"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new presion', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	setTimeout(function(){
		Sensor.findOne({paramSensor: "uv"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new uv', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	res.sendFile(__dirname + '/views/index.html');
});
//ruteo a flora y fauna
app.get('/flora-fauna',function(req,res){
	setTimeout(function(){
		Sensor.findOne({paramSensor: "alerta"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new alerta', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	res.sendFile(__dirname + '/views/flora-fauna.html');
});
//ruteo a informacion-general
app.get('/informacion-general',function(req,res){
	setTimeout(function(){
		Sensor.findOne({paramSensor: "alerta"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new alerta', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	res.sendFile(__dirname + '/views/informacion-general.html');
});
//ruteo a normas-del-parque
app.get('/normas-del-parque',function(req,res){
	setTimeout(function(){
		Sensor.findOne({paramSensor: "alerta"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new alerta', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	res.sendFile(__dirname + '/views/normas-del-parque.html');
});
//ruteo a rutas
app.get('/rutas',function(req,res){
	setTimeout(function(){
		Sensor.findOne({paramSensor: "alerta"},null,{sort:{fechaYHora: -1}},function(err,sensor){
			if(sensor!=null){
				io.sockets.emit('new alerta', {
					value: sensor.dato.toString(),
                                        time: sensor.fechaYHora.toString()
				});
			}
		});
	}, 1000);
	res.sendFile(__dirname + '/views/rutas.html');
});
//ruteo a chat
app.get('/chat', function(req, res) {
	res.redirect('http://192.168.252.250/chat');
});
