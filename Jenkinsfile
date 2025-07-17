pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'  // Local virtual environment directory
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                    if not exist .venv (
                        python -m venv .venv
                    )
                    call .venv\\Scripts\\activate
                    pip install --quiet --no-input --disable-pip-version-check --requirement requirements.txt
                '''
            }
        }

        stage('Run OpenCart Tests') {
            steps {
                echo 'Running Selenium tests for OpenCart...'
                bat '''
                    call .venv\\Scripts\\activate
                    pytest -v -s testcases/ --browser firefox --alluredir=allurereports
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            archiveArtifacts artifacts: 'reports/*.html, screenshots/*.png, logs/*.log', fingerprint: true

            // Allure report publishing
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allurereports']]
            ])
        }

        success {
            echo 'All tests passed!'
        }

        failure {
            echo 'Test or setup failed. Check logs.'
        }
    }
}
