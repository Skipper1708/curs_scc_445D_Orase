pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build - Creare mediu virtual Python si instalare dependinte'
                // Reconstruim curat mediul virtual si instalam pachetele
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r quickrequirements.txt
                '''
            }
        }
        
        stage('Calitate Cod') {
            steps {
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=.
                    pylint --exit-zero app/lib/biblioteca_orase.py
                    pylint --exit-zero app/tests/test_lib_orase.py
                    pylint --exit-zero orase.py
                '''
            }
        }
        
        stage('Testare') {
            steps {
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=.
                    pytest app/tests/ -v
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker build -t orase_manchester:latest .'
                sh 'docker stop orase_container || true'
                sh 'docker rm orase_container || true'
                sh 'docker run -d --name orase_container -p 8020:5011 orase_manchester:latest'
            }
        }
    }

    post {
        success { echo 'Pipeline finalizat cu succes!' }
        failure { echo 'Pipeline esuat. Verificati logurile.' }
    }
}