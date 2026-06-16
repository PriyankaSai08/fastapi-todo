pipeline {
    agent any

    environment{
        IMAGE_NAME="todo-app"
        CONTAINER_NAME="todo-app"
    }

    stages {
       
        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Tests') {
            steps {
                bat "docker run --rm %IMAGE_NAME% python -m pytest -v"
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
