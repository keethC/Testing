pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build APP'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Test APP'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploy APP'
            }
        }
    }

    post {
        always {
            emailext body: '''We regret to inform you that the [Process Name] encountered an unexpected failure during execution on [Date/Time]. Our team is currently investigating the issue and will work to resolve it as soon as possible.

We apologize for any inconvenience caused and appreciate your patience.''', 
            subject: 'Pipeline failure', 
            to: 'avkeeth29@gmail.com'
        } 
    }
}
