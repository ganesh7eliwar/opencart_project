pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root' // Run as root to fix apt-get permissions
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
                    echo "Updating package list and installing venv..."
                    apt-get update && apt-get install -y python3-venv

                    echo "Creating virtual environment..."
                    if [ ! -d "$VENV_DIR" ]; then
                      python3 -m venv $VENV_DIR
                    fi

                    echo "Activating virtual environment and installing dependencies..."
                    . $VENV_DIR/bin/activate

                    if [ -f requirements.txt ]; then
                      pip install --upgrade pip
                      pip install -r requirements.txt
                    else
                      echo "requirements.txt not found. Skipping pip install."
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Activating virtual environment and running tests..."
                    . $VENV_DIR/bin/activate

                    # Your custom test command
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
// This Jenkinsfile defines a pipeline that uses a Docker container with Python 3.12
// to set up a virtual environment, install dependencies, and run tests.