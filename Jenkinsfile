pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install streamlit pandas'
            }
        }

        stage('Run App Check') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
