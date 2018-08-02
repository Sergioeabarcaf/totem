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

## V0.9.1

Esta versión contiene las siguientes caracteristicas:
* Instalacion limpia de NodeJS 8.11.3 (NVM), mosquitto 1.5, MongoDB 2.4.14 sobre Raspbian 9 (stretch)
* Se levantan los servidores y servicio NodeJS desde el arranque con Bash y crontab
* Reorganizacion de las carpetas y orden de componentes
* Almacenamiento de log a nivel local y no correspondiente a git de todos los archivos que lo requieren
* se cambia el python de ejecucion de sensores por un bash
* eliminacion de archivos copiados basura
* cambio de nombre en archivos de sensores, teniendo el nombre del sensor utilizado
* carpeta test-sensores muestra los valores por pantalla y los almacena en un log local

## V0.9.2
Esta versión contiene las siguientes caracteristicas
* Reparación en bash que no permitia obtener presion
* reparacion en crontab que no permitia ejecutar bash getData
* Chmod +x para ejecucion de los archivos
* Eliminacion de registerON.py ya que el registro de fecha de encendido lo realiza el bash totem
* uso de mongoose V4.13.14 por compatibilidad con MongoDB 2.4.14

Versión estable funcionando desde el 30/Julio/2018 en Proteinlab
