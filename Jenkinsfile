pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build stage - verific proiectul'
                sh 'python3 --version'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv .venv_jenkins'
                sh '. .venv_jenkins/bin/activate && pip install --upgrade pip'
                sh '. .venv_jenkins/bin/activate && pip install flask pytest'
            }
        }

        stage('Test') {
            steps {
                sh '. .venv_jenkins/bin/activate && pytest'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deployment stage - aplicația este pregătită'
            }
        }
    }
}
