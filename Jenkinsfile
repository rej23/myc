pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'newtoken', url: 'https://github.com/rej23/myc.git']])
            }
        }
        
        stage('list files') {
            steps {
                git branch: 'master' , credentialsId: 'newtoken', url: 'https://github.com/rej23/myc.git'
                
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

        stage('Check PATH') {
            steps {
                sh 'echo $PATH'
            }
        }
        
        stage('Run Docker Command') {
            steps {
                sh '/usr/bin/docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'echo "b435936ae1c542528acca29fade62ce8" docker build -t my-docker-image .'
            }
        }

        stage('build') {
            steps {
                dir('Aprojet'){
                sh 'echo "b435936ae1c542528acca29fade62ce8" docker-compose build'
            
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('Aprojet'){
                sh 'echo "b435936ae1c542528acca29fade62ce8" docker-compose up'
            
                }
            }
        }
        
        stage('Build again') {
            steps {
                dir('Aprojet'){
                sh 'docker-compose up -d'
            
                }
            }
        }
    }
}
