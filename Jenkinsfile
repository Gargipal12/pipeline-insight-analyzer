pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Gargi\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install streamlit pandas'
            }
        }

        stage('Run App Check') {
            steps {
                bat '"C:\\Users\\Gargi\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py'
            }
        }
    }
}
