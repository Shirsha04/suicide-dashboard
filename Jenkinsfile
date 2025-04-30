pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/YourUsername/suicide-dashboard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t suicide-dashboard .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    sh 'docker tag suicide-dashboard $USERNAME/suicide-dashboard'
                    sh 'docker push $USERNAME/suicide-dashboard'
                }
            }
        }
    }
}
