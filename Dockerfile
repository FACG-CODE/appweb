# Imagen base, usamos Python 3.11 slim para un contenedor liviano
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .

# Instalamos las dependencias usando pip, sin cache para mantener el contenedor más liviano
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ .

# Exponer puerto de Flask, indica que la app corre en el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "-u", "main.py"]