pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build proiect Orașe - București'
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Pylint') {
            steps {
                echo 'Verificare statica folosind pylint'
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/tests/*.py
                    pylint --exit-zero orase.py
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Rulare teste unitare cu pytest'
                sh '''
                    . .venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Creare imagine Docker'
                sh '''
                    docker build -t orase-paunoiu-ianis .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Pornire container Docker'
                sh '''
                    docker rm -f container-orase-paunoiu-ianis || true
                    docker run -d -p 5011:5011 --name container-orase-paunoiu-ianis orase-paunoiu-ianis
                    docker ps
                '''
            }
        }
    }
}
