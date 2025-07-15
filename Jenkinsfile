pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root'  // Needed to install system packages like Chrome
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

        stage('Setup Environment') {
            steps {
                sh '''
                    echo "Updating package list and installing dependencies..."
                    apt-get update && apt-get install -y wget curl gnupg python3-venv

                    echo "Installing Google Chrome..."
                    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
                    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
                    apt-get update
                    apt-get install -y google-chrome-stable

                    echo "Creating Python virtual environment..."
                    if [ ! -d "$VENV_DIR" ]; then
                        python3 -m venv $VENV_DIR
                    fi

                    echo "Activating virtual environment and installing Python dependencies..."
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Activating virtual environment and running tests..."
                    . $VENV_DIR/bin/activate

                    pytest -v -s testcases/ --browser chrome
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up...'
        }
        success {
            echo '✅ Build and tests completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}
// Jenkinsfile for Python project with Docker and Google Chrome
// This Jenkinsfile sets up a Docker environment, installs Google Chrome, creates a Python virtual environment