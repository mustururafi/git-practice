pipeline {
    agent any

    environment {
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

        stage('Automated Tests') {
            steps {
                sh 'python3 --version'
                sh 'python3 test_website.py'
            }
            post {
                always {
                    junit 'junit-report.xml'
                }
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

        stage('Trivy Security Scan') {
            steps {
                sh '''
                    trivy image \
                      --severity HIGH,CRITICAL \
                      --ignore-unfixed \
                      --exit-code 0 \
                      ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Security Gate') {
            steps {
                sh '''
                    trivy image \
                      --severity HIGH,CRITICAL \
                      --ignore-unfixed \
                      --exit-code 1 \
                      ${IMAGE_NAME}:${IMAGE_TAG}
                '''
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
            echo 'Image passed Trivy security checks and was deployed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs and Trivy security report.'
        }
    }
}
