pipeline {
    agent any
    stages {
        stage('cloning') {
            steps {
                bat 'git clone https://github.com/shwetanshusingh2/s3bucketcopy'
                
            }
        }
         stage('executing') {
            steps {
                
                bat 'python helper.py'
               
            }
        }
          stage('deletion') {
            steps {
                bat 'rmdir /Q /S s3bucketcopy'
            }
        }
        
        
        
        
    }
}
