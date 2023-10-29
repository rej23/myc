pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '46e0404e-2827-45a4-9210-665f38fc1482', url: 'https://github.com/rej23/myc.git']])
            }
        }
        
        stage('list files') {
            steps {
                git branch: 'master' , credentialsId: '46e0404e-2827-45a4-9210-665f38fc1482', url: 'https://github.com/rej23/myc.git'
                
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

// LEARN HOW TO INSTALL DOCKER USING PIPELINES


        // stage('Install Docker') {
        //     steps {
        //         sh 'curl -fsSL https://get.docker.com -o get-docker.sh'
        //         sh 'echo "3882b2b6956248cebf60b4a33da3faef" sh get-docker.sh'
        //     }
        // }

        // stage('Install Docker Compose') {
        //     steps {
        //         sh 'echo "3882b2b6956248cebf60b4a33da3faef" curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
        //         sh 'echo "3882b2b6956248cebf60b4a33da3faef" chmod +x /usr/local/bin/docker-compose'
        //     }
        // }

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
                sh 'docker-compose up'
            
                }
            }
        }

    }
}