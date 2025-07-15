pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '--env WDM_LOCAL=1'
        }
    }

    environment {
        PYTHON = 'python3'
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
                sh """
                    ${PYTHON} -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    ${PYTHON} -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate
                    pytest -v -s testcases/ --browser=chrome
                """
            }
        }
    }

    post {
        always {
            sh """
                . ${VENV_DIR}/bin/activate
                pip freeze > requirements.txt
            """
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs.'
        }
    }
}