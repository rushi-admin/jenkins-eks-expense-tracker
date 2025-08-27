pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhubcreds')
        GITHUB_CREDENTIALS = credentials('githubcreds')
        KUBE_CONFIG_CREDENTIALS = credentials('eks-kubeconfig')
        DOCKER_IMAGE = "rushiadmin/expense-tracker:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/rushi-admin/jenkins-eks-expense-tracker.git',
                    credentialsId: 'githubcreds'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                        echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                        docker push $DOCKER_IMAGE
                    """
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    writeFile file: 'kubeconfig', text: KUBE_CONFIG_CREDENTIALS
                    sh 'export KUBECONFIG=$WORKSPACE/kubeconfig'
                    sh 'kubectl apply -f deployment.yaml -n test'
                    sh 'kubectl apply -f service.yaml -n test'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Expense Tracker deployed successfully to EKS!'
        }
        failure {
            echo '❌ Deployment failed. Check logs for errors.'
        }
    }
}
