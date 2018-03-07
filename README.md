# Proyecto Totem Turismo

Este repositorio corresponde a los elementos contenido en Raspberry Pi de Torre, por ende, desde este repositorio se activan los siguientes servicios:
* Servidor web para levantar portal de visitas
* Sistema de obtencion de datos desde la estacion metereologica
* base de dato en MongoDB que almacena los datos obtenidos por la estacion metereologica

Este proyecto esta desarrollado con NodeJS y utiliza:
* Servidor MQTT mosquitto - (mqtt)
* Socket para comunicacion en tiempo real de los mensajes en sistema de mensajeria grupal y datos obtenidos de la estacion metereologica. - (socket.io)
* MongoDB para el almacenamiento de los datos obtenidos de la estacion metereologica - (mongoose)

## V0.9
Esta version del sistema esta probada en la experiencia realizada en Rio Clarillo el 25 de enero de 2018.

* Falta pasar a produccion.

### errores y/o mejoras aplicables
* Ejecutar los servicios desde el inicio pero sin crontab como esta actualmente
* mejorar interfaces graficas
