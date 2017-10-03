# Layout de totem para proteinlab

## Uso
El layout se encuentra modularizado para su utilización en cualquier entorno de desarrollo.
Los archivos necesarios son los siguientes:
* index.html 
* css/app.css

## instalación de entorno de desarrollo

Para poder editar el css de este layout es necesario tener:

- [NodeJS](https://nodejs.org/en/) (0.12 o mayor)
- [Git](https://git-scm.com/)

Para instalar todas las dependencias es necesario ejecutar lo siguiente en el directorio raiz

```bash
npm install
bower install
```

Para poder ejecutar el compilador de sass y las tareas de watch sobre cambios de archivo es necesario tener el CLI de foundation o en su defecto Gulp

### Usando el CLI de foundation

Instala el CLI de foundation con el siguiente comando

```bash
npm install foundation-cli --global
```

una vez instalado ejecutar el siguiente comando para iniciar el compilador/watch

```bash
foundation watch
```

### Usando Gulp

Instalar Gulp de manera global 

```bash
npm install gulp --global
```

ejecutar el compilador/watch

```bash
gulp
```
