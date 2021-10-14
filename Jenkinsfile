pipeline {
    agent { label 'qa-tag' }
    environment {
        NEXUS_USER = credentials("nexus_user")
        NEXUS_PASSWORD = credentials("nexus_password")
        TOKEN = credentials("gitlab-svc-token")
    }

    stages {
         stage("Tag Release") {
            steps {
                script {
                    dir("interpreta") {
                       echo "In Tag Release stage" 
                       sh "python tagBuild1.py"
                       echo "Tag complete!"
                        }
                    }

                }
            }

        }

    }
   
