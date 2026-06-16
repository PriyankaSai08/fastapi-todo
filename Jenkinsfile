pipeline {
    agent any

    environment{
        IMAGE_NAME="todo-app"
        CONTAINER_NAME="todo-app"
    }

    stages {
       stage('Debug') {
            steps {
                bat "docker run --rm todo-app dir"
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Tests') {
        steps {
            withCredentials([
                string(credentialsId: 'DATABASE_URL', variable: 'DATABASE_URL'),
                string(credentialsId: 'DATABASE_URL_TEST', variable: 'DATABASE_URL_TEST')
            ]) {
                bat '''
                docker run --rm ^
                -e DATABASE_URL=%DATABASE_URL% ^
                -e DATABASE_URL_TEST=%DATABASE_URL_TEST% ^
                %IMAGE_NAME% python -m pytest -v
                '''
            }
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
