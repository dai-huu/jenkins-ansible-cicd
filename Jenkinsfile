pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        GITHUB_CREDENTIALS = credentials('github-credentials')
        DOCKER_IMAGE = 'daihuu103/django-hello-world'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
                sh 'docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                sh 'echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}'
                sh 'docker push ${DOCKER_IMAGE}:latest'
            }
        }
        
        stage('Deploy with Ansible') {
            when {
                branch 'main'
            }
            steps {
                sh 'ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/deploy.yml'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
