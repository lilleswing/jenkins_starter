pipeline {
    agent {
        any {
        }
    }
    stages {
        stage('Run') {
            steps {
                sh '''#!/bin/bash
                bash devtools/jenkins.sh
                '''
            }
        }
    }
    post {
            always {
                junit 'nosetests.xml'
            }
            failure {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        emailext attachLog: true, body: '$DEFAULT_CONTENT', to: 'karl.leswing@gmail.com', recipientProviders: [], subject: '$DEFAULT_SUBJECT'
                    }
                }
            }
    }
}
