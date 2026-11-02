
pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
        IMAGE_NAME = 'rafi-jenkins-demo'
        IMAGE_TAG = '2.0'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker version'
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Verify Image') {
            steps {
                sh 'docker images ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }
    }

    post {
        success {
            echo 'Docker image built successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
