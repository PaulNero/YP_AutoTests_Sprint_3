pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.10'
    }
    stages {
        stage('pull_code') {
            steps {
                echo 'Pulling code...'
                git url: 'https://github.com/PaulNero/yp-autotests-sprint-3.git', branch: 'main'
            }
        }
        stage('prepare_environment') {
            steps {
                echo 'Preparing environment...'
                writeFile file: '.env', text: "NAME=${NAME}\nPASSWORD_RIGHT=${PASSWORD_RIGHT}\nPASSWORD_6_SYMBOLS=${PASSWORD_6_SYMBOLS}\nPASSWORD_WRONG=${PASSWORD_WRONG}\nDELAY=${DELAY}\nEMAIL_FOR_LOGIN=${EMAIL_FOR_LOGIN}\nMAIN_LINK=${MAIN_LINK}"
            }
        }
        stage('install_dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install poetry' || true
                sh 'poetry install' || true
            }
        }
        stage('run_tests') {
            steps {
                echo 'Running tests...'
                sh 'poetry run pytest'
            }
        }
    }
    triggers {
        githubWebhook()
        pollSCM('H/6 * * * *')
    }
}