pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build - creare mediu virtual Python'
                sh '. ./activeaza_venv_jenkins'
            }
        }
        stage('Calitate Cod') {
            steps {
                sh '. .venv/bin/activate && pylint --exit-zero app/lib/*.py'
                sh '. .venv/bin/activate && pylint --exit-zero app/tests/*.py'
                sh '. .venv/bin/activate && pylint --exit-zero orase.py'
            }
        }
        stage('Testare') {
            steps {
                sh '. ./activeaza_venv && pytest app/tests/ -v'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t orase_viena:latest .'
                sh 'docker stop orase_container || true'
                sh 'docker rm orase_container || true'
                sh 'docker run -d --name orase_container -p 5011:5011 orase_viena:latest'
            }
        }
    }

    post {
        success { echo 'Pipeline finalizat cu succes!' }
        failure { echo 'Pipeline esuat. Verificati logurile.' }
    }
}
