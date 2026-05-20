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
                // Activam mediul si rulam pylint in aceeasi comanda structurata pe mai multe linii (folosind ghilimele triple)
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/biblioteca_orase.py
                    pylint --exit-zero app/tests/test_lib_orase.py
                    pylint --exit-zero orase.py
                '''
            }
        }
        
        stage('Testare') {
            steps {
                // Rulam pytest asigurarandu-ne ca suntem in interiorul mediului virtual activat
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/ -v
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker build -t orase_manchester:latest .'
                sh 'docker stop orase_container || true'
                sh 'docker rm orase_container || true'
                sh 'docker run -d --name orase_container -p 5011:5011 orase_manchester:latest'
            }
        }
    }

    post {
        success { echo 'Pipeline finalizat cu succes!' }
        failure { echo 'Pipeline esuat. Verificati logurile.' }
    }
}