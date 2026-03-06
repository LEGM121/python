# Imagen base de Python 3.13 en su versión ligera
FROM python:3.13-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar e instalar dependencias primero (optimiza caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente
COPY . .

# Puerto que expone la aplicación
EXPOSE 5000

# Comando para arrancar la aplicación con gunicorn (servidor de producción)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
