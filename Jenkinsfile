pipeline {
    agent any

    stages {
        stage('Load Config') {
            steps {
                script {
                    def props = readProperties file: '.env'

                    env.IMAGE_NAME = props['IMAGE_NAME']
                    env.CONTAINER_NAME = props['CONTAINER_NAME']
                }
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Tests') {
            steps {
                bat "docker run --rm %IMAGE_NAME% pytest -v"
            }
        }

        stage('Deploy') {
            steps {
                bat "docker stop %CONTAINER_NAME% || exit 0"
                bat "docker rm %CONTAINER_NAME% || exit 0"
                bat "docker run -d --name %CONTAINER_NAME% -p 8000:8000 %IMAGE_NAME%"
            }
        }
    }
}
