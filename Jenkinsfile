pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirement.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'PYTHONPATH=. python -m unittest discover -s app/test'
            }
        }
    }
}
