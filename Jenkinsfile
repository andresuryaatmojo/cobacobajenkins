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
                    sh '''
                    #!/bin/bash
                    source $VENV/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Project...'
                sh '''
                #!/bin/bash
                source $VENV/bin/activate
                python -c "print(\\"Dummy build step executed\\")"
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh '''
                #!/bin/bash
                source $VENV/bin/activate
                pytest -v
                '''
            }
        }
        stage('Lint') {
            steps {
                echo 'Linting the Code...'
                sh '''
                #!/bin/bash
                source $VENV/bin/activate
                pylint **/*.py
                '''
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
            sh 'deactivate'
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
