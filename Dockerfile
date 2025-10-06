# Imagen base con Python 3.11
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la carpeta src completa
COPY src/ .

# Exponer puerto de Flask
EXPOSE 5000

# Ejecutar Flask en foreground
CMD ["python", "-u", "main.py"]
