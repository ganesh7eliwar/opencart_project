pipeline {
    agent {
        docker {
            image 'opencart-python:latest'
            args '-u root'
        }
    }

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests..."
                    pytest -v -s testcases/ --browser chrome
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo '✅ Tests passed.'
        }
        failure {
            echo '❌ Tests failed.'
        }
    }
}