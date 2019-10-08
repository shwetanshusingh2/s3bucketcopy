pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'rmdir /Q /S s3bucketcopy'
                bat 'git clone https://github.com/shwetanshusingh2/s3bucketcopy'
                bat 'python s3bucketcopy/helper.py'
            }
        }
    }
}
