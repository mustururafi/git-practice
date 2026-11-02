
pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
        KUBECONFIG = '/var/jenkins_home/.kube/config'
        IMAGE_NAME = 'rafi-jenkins-demo'
        IMAGE_TAG = "${BUILD_NUMBER}"
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

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl get nodes'
                sh 'kubectl set image deployment/rafi-jenkins-demo website=${IMAGE_NAME}:${IMAGE_TAG}'
                sh 'kubectl rollout status deployment/rafi-jenkins-demo'
            }
        }
    }

    post {
        success {
            echo 'Docker image built and deployed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
