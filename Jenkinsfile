// Pipeline CD - Entrega Continua
// Define los stages para construir y publicar la imagen Docker en DockerHub

pipeline {
  agent any

  // Variables del pipeline
  environment {
    C_IMAGE_NAME      = 'devops-app'
    C_IMAGE_TAG       = 'latest'
    C_REPO_URL        = 'https://github.com/GeronimoAv/lab-CI-CD-devops.git'
    C_DOCKER_REGISTRY = 'docker.io'
  }

  stages {

    // Stage 1: Clonar el repositorio
    stage('Clonar repositorio') {
      steps {
        git branch: 'main', url: env.C_REPO_URL
      }
    }

    // Stage 2: Construir la imagen Docker
    stage('Construir imagen Docker') {
      steps {
        sh 'docker build -t ' + env.C_IMAGE_NAME + ':' + env.C_IMAGE_TAG + ' .'
      }
    }

    // Stage 3: Publicar la imagen en DockerHub
    stage('Publicar imagen en DockerHub') {
      steps {
        withCredentials([
          string(credentialsId: 'dockerhub-user', variable: 'V_DOCKER_USER'),
          string(credentialsId: 'dockerhub-pass', variable: 'V_DOCKER_PASS')
        ]) {
          sh 'echo $V_DOCKER_PASS | docker login ' + env.C_DOCKER_REGISTRY + ' -u $V_DOCKER_USER --password-stdin'
          sh 'docker tag ' + env.C_IMAGE_NAME + ':' + env.C_IMAGE_TAG + ' $V_DOCKER_USER/' + env.C_IMAGE_NAME + ':' + env.C_IMAGE_TAG
          sh 'docker push $V_DOCKER_USER/' + env.C_IMAGE_NAME + ':' + env.C_IMAGE_TAG
        }
      }
    }

  }

  post {
    success {
      echo 'Pipeline CD ejecutado correctamente'
    }
    failure {
      echo 'Pipeline CD falló'
    }
  }
}
