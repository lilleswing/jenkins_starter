pipeline {
    agent {
        any {
        }
    }
    triggers {
        cron(env.BRANCH_NAME == 'master' ? '0 H * * *' : '')
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
                try {
                    junit 'nosetests.xml'
                } catch (err) {
                    echo "Caught: ${err}"
                }
                try {
                    deleteDir()
                } catch (err) {
                    echo "Caught: ${err}"
                }
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
