# 🚀 Proyecto Flask + Nginx + MySQL

Aplicación web desarrollada con **Flask**, servida detrás de **Nginx**, conectada a una base de datos **MySQL**, lista para desplegar en contenedores Docker.

---

## 🛠 Tecnologías

* Python 3.11 + Flask
* MySQL 8.0
* Nginx
* Docker / Docker Compose
* HTML + Bootstrap (templates Flask)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat\&logo=docker\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)

---

## 📂 Estructura del proyecto

```
appweb/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── src/
    ├── main.py
    └── templates/
        └── index.html
```

---

## ⚡ Cómo correr la aplicación

# 1️⃣ Instalación y verificación
wsl --install         # Instala WSL2 si no está
wsl --update          # Actualiza WSL2 si hace falta
docker --version      # Verifica Docker
docker compose version
docker run hello-world
docker login          # Inicia sesión en Docker Hub

# 2️⃣ Descargar imagenes y crear red privada
# a. Descargar las imágenes necesarias
docker pull mysql:8.0
docker pull nginx
docker pull facg/appweb:1.0

# b. Crear la red de Docker (si aún no la tienes)
docker network create webapp-net

# 3️⃣ Levantar contenedores a partir de imagenes descargadas y conectarlos a la red privada
# a. MySQL
docker run -d --name mysqlserver \
-e MYSQL_ROOT_PASSWORD=12345 \
-p 3306:3306 \
--network webapp-net \
mysql:8.0

# b. Nginx
docker run -d --name webserver \
-p 8080:80 \
--network webapp-net \
nginx

# c. Flask (appweb)
docker run -d --name appweb --network webapp-net facg/appweb:1.0

# 4️⃣ Configuración de Nginx para Flask e Inicializacion de la base de datos con MySQL Workbench
# a. Crear archivo "nginx.conf" que contenga las siguientes lineas:
server {
    listen 80;

    location / {
        proxy_pass http://appweb:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# b. Copiar nginx.conf al contenedor
docker cp <ruta del archivo .conf creado> webserver:/etc/nginx/conf.d/default.conf

# c. Entrar al contenedor y verificar
  docker exec -it webserver sh
  nginx -t
  nginx -s reload
  exit
# d. Abrir MySQL Workbench y crear una nueva conexión:
  Hostname / IP: localhost
  Puerto: 3306
  Usuario: root
  Contraseña: 12345
# e. Crear base de datos con el siguiente script sql:
  create database if not exists practica_docker;
  use practica_docker;

  create table usuarios (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    correo varchar(100) not null
  );

  /* INSERT DE TABLA USUARIOS */
  insert into usuarios (nombre, apellido, correo) values
    ('Francisco', 'Cruz', 'franciscocruz@gmail.com'),
    ('Agustin', 'Guantay', 'agustinguantay@gmail.com'),
    ('Estefania', 'Gutierrez', 'estefaniagutierrez@gmail.com'),
    ('Ivan', 'Gutierrez', 'ivangutierrez@gmail.com');
    
# 5️⃣ Verificación de servicios: La pagina debe mostrar un titulo y una tabla con los datos cargados en la base de datos.
Abrir navegador: http://localhost:8080

# 🔹 Extra: Imágenes de uso de consola
Link: https://drive.google.com/drive/folders/1Bs9oBEZLvbuumyVKO-zc_zq7jN2vSwsV?usp=sharing
