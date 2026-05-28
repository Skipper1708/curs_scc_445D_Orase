pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build - pregatire mediu Python'
                sh 'python3 -m venv .venv || true'
                sh '. .venv/bin/activate && pip install -r requirement.txt'
                sh '. .venv/bin/activate && pip install pylint pytest'
            }
        }

        stage('Calitate Cod') {
            steps {
                sh '. .venv/bin/activate && pylint --exit-zero orase.py'
                sh '. .venv/bin/activate && pylint --exit-zero app/lib/*.py'
                sh '. .venv/bin/activate && pylint --exit-zero app/routes/*.py'
                sh '. .venv/bin/activate && pylint --exit-zero app/test/*.py'
            }
        }

        stage('Testare') {
            steps {
                sh '. .venv/bin/activate && PYTHONPATH=. python -m unittest discover -s app/test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker build -t orase-paris-app:latest .'
                sh 'docker stop orase-paris-container || true'
                sh 'docker rm orase-paris-container || true'
                sh 'docker run -d --name orase-paris-container -p 5000:5000 orase-paris-app:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes!'
        }

        failure {
            echo 'Pipeline esuat. Verificati logurile.'
        }
    }
}
