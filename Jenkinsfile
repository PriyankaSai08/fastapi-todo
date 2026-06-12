pipeline{
    agent any
    environment{
        IMAGE_NAME = "todo-app"
        CONTAINER_NAME = "todo-app"
    }
    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
            
        }
        stage(build docker image){
            steps{
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
        stage('Run Tests'){
            steps{
                sh docker run --rm ${IMAGE_NAME} pytest -v"

            }
        }
        stage('Deploy'){
            steps{
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                sh "docker run-d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}"}
                }}

    }
}