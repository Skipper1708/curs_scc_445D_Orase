pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Build - creare mediu virtual Python'
                sh 'ls -la'
                sh '. ./activeaza_venv_jenkins'
            }
        }

        stage('Calitate Cod') {
            steps {
                echo 'Analiza statica cu pylint'
                sh '. .venv/bin/activate && pylint --exit-zero app/lib/*.py'
                sh '. .venv/bin/activate && pylint --exit-zero app/tests/*.py'
                sh '. .venv/bin/activate && pylint --exit-zero orase.py'
            }
        }

        stage('Testare') {
            steps {
                echo 'Rulare unit-teste cu pytest'
                sh '. ./activeaza_venv && pytest app/tests/ -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Creare imagine Docker si pornire container'
                sh 'docker build -t orase_barcelona:latest .'
                sh 'docker stop orase_container || true'
                sh 'docker rm orase_container || true'
                sh 'docker run -d --name orase_container -p 5011:5011 orase_barcelona:latest'
                echo 'Container pornit pe portul 5011'
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
