pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    ls -l app
                    ls -l app/lib
                    ls -l app/teste
                    python3 -m venv .venv
                    .venv/bin/pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Testare - pylint si pytest') {
            agent any
            steps {
                sh '''
                    .venv/bin/pylint --exit-zero app/lib/biblioteca_orase.py
                    .venv/bin/pylint --exit-zero orase.py
                    PYTHONPATH=$WORKSPACE:$WORKSPACE/app/lib .venv/bin/pytest
                '''
            }
        }

        stage('Deploy - Docker') {
            agent any
            steps {
                echo 'Building and starting Docker container...'
                sh '''
                    docker build -t orase-lisabona .
                    docker stop orase-lisabona-container || true
                    docker rm orase-lisabona-container || true
                    docker run -d --name orase-lisabona-container -p 5011:5011 orase-lisabona
                '''
            }
        }
    }
}
