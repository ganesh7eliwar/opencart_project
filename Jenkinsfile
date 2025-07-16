pipeline {
    agent any  // Use any available agent (local Jenkins or connected node)

    environment {
        VENV_DIR = '.venv'  // Local virtual environment directory
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                bat '''
                    if not exist %VENV_DIR% (
                        python -m venv %VENV_DIR%
                    )
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run OpenCart Tests') {
            steps {
                echo '🧪 Running Selenium tests for OpenCart...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pytest -v -s testcases/ --browser chrome
                '''
            }
        }
    }

    post {
        always {
            echo '📦 Pipeline completed (success or failure).'
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Test or setup failed. Check logs.'
        }
    }
}
