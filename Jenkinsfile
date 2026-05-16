pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r quickrequirements.txt --break-system-packages'
            }
        }
        stage('Test') {
            steps {
                sh 'cd ${WORKSPACE} && python3 -m pytest app/teste/test_como.py -v'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t como-app .'
                sh 'docker stop como-app || true'
                sh 'docker rm como-app || true'
                sh 'docker run -d -p 5000:5000 --name como-app como-app'
            }
        }
    }
}
