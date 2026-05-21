pipeline {
    agent any

    environment {
        IMAGE_NAME = "orase_viena_urmuz_laurentiu"
        CONTAINER_NAME = "container_viena_urmuz"
        PORT_HOST = "8020"
        PORT_CONTAINER = "5011"
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME} ."
                echo 'Build finished.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh "docker run --rm ${IMAGE_NAME} python3 -m pytest app/tests/ -v"
                echo 'Tests finished.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT_HOST}:${PORT_CONTAINER} ${IMAGE_NAME}"
                echo "Application running at http://127.0.0.1:${PORT_HOST}"
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
