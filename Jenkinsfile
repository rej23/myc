pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'f50884ed-463b-47e1-8be9-ff6c9c2ad757', url: 'https://github.com/rej23/myc.git']])
            }
        }
        
        stage('list files') {
            steps {
                git branch: 'master' , credentialsId: 'f50884ed-463b-47e1-8be9-ff6c9c2ad757', url: 'https://github.com/rej23/myc.git'
                
                sh 'ls > file_list.txt'
                sh 'cat file_list.txt'
            
            }
        }
        
        stage('Navigate to folder') {
            steps {
                dir('Aprojet'){
                sh 'ls > file_list.txt'
                sh 'cat file_list.txt'
                }
            }
        }
        
        stage('check file') {
            steps {
                script{
                    if(sh(script: 'ls Aprojet/manage.py', returnStatus:true)==0){
                        echo "file exist"
                    } else { error "file does not exist"
                    }
                }
            }
        }

        stage('check file 2') {
            steps {
                script{
                    if(sh(script: 'ls Aprojet/Dockerfile', returnStatus:true)==0){
                        echo "file exist"
                    } else { error "file does not exist"
                    }
                }
            }
        }


        stage('Install Docker') {
            steps {
                sh 'curl -fsSL https://get.docker.com -o get-docker.sh'
                sh 'sudo sh get-docker.sh'
            }
        }

        stage('Install Docker Compose') {
            steps {
                sh 'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
                sh 'sudo chmod +x /usr/local/bin/docker-compose'
            }
        }
        
        //  stage('Build') {
        //     steps {
        //         dir('Aprojet'){
        //         sh 'docker-compose build'
            
        //         }
        //     }
        // }

        // stage('Deploy') {
        //     steps {
        //         dir('Aprojet'){
        //         sh 'docker-compose up -d'
            
        //         }
        //     }
        // }

    }
}