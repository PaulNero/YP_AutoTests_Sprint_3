pipeline {
    agent {
        docker {
            image 'nerobovp/npn-test-chrome-python-allure:latest'
            args '--network host --shm-size=2g -v /var/lib/jenkins/.cache/pypoetry:/home/tester/.cache/pypoetry'
        }
    }

    parameters {
        string(name: 'RUN-TYPE', defaultValue: 'auto', description: 'Type of run: auto or manual')
    }

    triggers {
        githubPush()
        pollSCM('H H/24 * * *')
    }

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Install dependencies') {
            steps {
                echo 'Installing project dependencies via Poetry...'
                sh '''
                    poetry install --no-root -vvv
                '''
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    poetry run pytest --maxfail=3 --disable-warnings -q --junitxml=pytest-results.xml --alluredir=allure-results
                    allure generate allure-results -o allure-report --clean
                '''
            }
            post {
                always {
                    junit 'pytest-results.xml'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Tests passed successfully!'
        }
        failure {
            echo '❌ Tests failed. Check the report above.'
        }
        cleanup {
            echo '🧹 Cleaning up temporary files...'
            sh 'rm -rf /home/tester/.cache/pip'
        }
    }
}
