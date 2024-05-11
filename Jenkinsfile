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
                    sh '. $VENV/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Project...'
                sh '. $VENV/bin/activate && python setup.py build'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh '. $VENV/bin/activate && pytest -v'
            }
        }
        stage('Lint') {
            steps {
                echo 'Linting the Code...'
                sh '. $VENV/bin/activate && pylint **/*.py'
            }
        }
        stage('Report') {
            steps {
                echo 'Generating Reports...'
                // Simulasikan generasi laporan atau gunakan plugin yang sesuai
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
            // Tambahkan langkah untuk mengirim notifikasi jika perlu
        }
    }
}
