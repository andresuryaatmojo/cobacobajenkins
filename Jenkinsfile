pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh 'python3 -m venv $VENV'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'source $VENV/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Project...'
                sh 'source $VENV/bin/activate && python -c "print(\\"Dummy build step executed\\")"'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'source $VENV/bin/activate && pytest -v'
            }
        }
        stage('Lint') {
            steps {
                echo 'Linting the Code...'
                sh 'source $VENV/bin/activate && pylint **/*.py'
            }
        }
        stage('Report') {
            steps {
                echo 'Generating Reports...'
                sh 'echo "Reports generated"'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
