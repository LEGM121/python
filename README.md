# Documentación Técnica - CI/CD DevOps

## Estructura del Proyecto

```
├── app.py                        # Código fuente Flask
├── Dockerfile                    # Imagen Docker
├── Jenkinsfile                   # Pipeline CD (Jenkins)
├── requirements.txt              # Dependencias Python
├── conftest.py                   # Configuración pytest
├── pytest.ini                    # Opciones pytest
├── tests/
│   └── test_app.py               # Pruebas unitarias
└── .github/
    └── workflows/
        └── ci.yml                # Pipeline CI (GitHub Actions)
```

---


## Flujo CI/CD

1. **CI (GitHub Actions):**
   - Se ejecuta automáticamente en cada push/pull request.
   - Stages:
     - Checkout del código
     - Instalación de dependencias
     - Ejecución de pruebas (pytest)
     - Build de imagen Docker

2. **CD (Jenkins):**
   - Pipeline definido en Jenkinsfile.
   - Stages:
     - Clonar repositorio
     - Construir imagen Docker
     - Publicar imagen en DockerHub
   - Automatización: Se puede activar por webhook o Poll SCM.

---

## Configuración y Ejecución

### CI - GitHub Actions
- Archivo: `.github/workflows/ci.yml`
- Disparador: push/pull request a main
- Pruebas: `pytest tests/ -v`
- Build Docker: `docker build -t devops-app .`

### CD - Jenkins
- Archivo: `Jenkinsfile`
- Credenciales: `dockerhub-user` y `dockerhub-pass` (Secret Text)
- Publicación: `docker push geronimoav/devops-app:latest`
- Automatización: Webhook GitHub o Poll SCM

---

## Pantallazos Requeridos

1. **pruebas unitarias**
   - ![PRUEBAS UNITARIAS](assets/image-6.png)
2. **Pipeline CI en GitHub Actions**
   - ![CI](assets/image-1.png)

3. **Pipeline CD en Jenkins**
   - ![CD](assets/image-2.png)

4. **DockerHub**
   - ![dockerhub](assets/image-3.png)
   - ![docker](assets/image-5.png)

5. **Aplicación corriendo en local**
   - Navegador en `http://localhost:5000` mostrando respuesta JSON
    ![APLICACION](assets/image-4.png)

---

## Tutorial: Cómo realizar pruebas

### Detener y eliminar contenedores por separado

Para detener solo Jenkins:
```bash
docker stop jenkins
```

Para eliminar solo Jenkins:
```bash
docker rm jenkins
```

Para detener solo la app:
```bash
docker stop devops-app
```

Para eliminar solo la app:
```bash
docker rm devops-app
```

Para detener todos los contenedores:
```bash
docker stop $(docker ps -q)
```

Para eliminar todos los contenedores detenidos:
```bash
docker rm $(docker ps -aq)
```

Para detener y eliminar Jenkins y la app juntos:
```bash
docker stop devops-app jenkins
docker rm devops-app jenkins
```

Puedes verificar que no queda nada corriendo con:
```bash
docker ps
```
(Puedes agregar esta sección antes de las pruebas o al inicio del tutorial)

### Creación de contenedores Docker

#### 1. Contenedor Jenkins

Para crear el contenedor Jenkins con acceso a Docker:

```bash
docker run -d --name jenkins -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

Esto permite que Jenkins ejecute comandos Docker desde el pipeline.

Accede a Jenkins en:
```
http://localhost:8080
```

#### 2. Contenedor de la aplicación

Para crear y ejecutar el contenedor de la app:

```bash
docker build -t devops-app:latest .
docker run -d --name devops-app -p 5000:5000 devops-app:latest
```

O desde DockerHub:
```bash
docker pull geronimoav/devops-app:latest
docker run -d --name devops-app -p 5000:5000 geronimoav/devops-app:latest
```

Accede a la app en:
```
http://localhost:5000
```

### 1. Instalar dependencias

Abre una terminal en la raíz del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar pruebas unitarias

Ejecuta las pruebas con pytest:

```bash
pytest tests/ -v
```

### 3. Probar la aplicación localmente

Construye y ejecuta la imagen Docker:

```bash
docker build -t devops-app:latest .
docker run -d --name devops-app -p 5000:5000 devops-app:latest
```

Abre tu navegador en:
```
http://localhost:5000
```
Deberías ver el mensaje JSON de bienvenida.

### 4. Probar la ruta de salud

En el navegador o usando curl:
```
http://localhost:5000/health
```
Respuesta esperada:
```
{"status": "healthy"}
```

### 5. Detener y eliminar el contenedor

```bash
docker stop devops-app
docker rm devops-app
```
