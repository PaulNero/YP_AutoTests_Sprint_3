pipeline {
    agent any
    parameters {
        string(name: 'RUN-TYPE', defaultValue: 'auto', description: 'Type of run: auto or manual')
    }
    triggers {
        githubPush()
        pollSCM('H/6 * * * *')
    }
    stages {
        stage('pull_code') {
            when {
                anyOf {
                    branch 'origin/main'
                    expression {
                        params['RUN-TYPE'] == 'manual'
                    }
                }
            }   
            steps {
                echo 'Pulling code...'
                git url: 'https://github.com/PaulNero/yp-autotests-sprint-3.git', branch: 'main'
            }
        }
        stage('prepare_environment') {
            when {
                anyOf {
                    branch 'origin/main'
                    expression {
                        params['RUN-TYPE'] == 'manual'
                    }
                }
            }
            steps {
                echo 'Preparing environment...'
                writeFile file: '.env', text: "NAME=${NAME}\nPASSWORD_RIGHT=${PASSWORD_RIGHT}\nPASSWORD_6_SYMBOLS=${PASSWORD_6_SYMBOLS}\nPASSWORD_WRONG=${PASSWORD_WRONG}\nDELAY=${DELAY}\nEMAIL_FOR_LOGIN=${EMAIL_FOR_LOGIN}\nMAIN_LINK=${MAIN_LINK}"
            }
        }
        stage('install_dependencies') {
            when {
                anyOf {
                    branch 'origin/main'
                    expression {
                        params['RUN-TYPE'] == 'manual'
                    }
                }
            }
            steps {
                echo 'Installing dependencies...'
                sh 'pip install poetry' || true
                sh 'poetry install' || true
            }
        }
        stage('run_tests') {
            when {
                anyOf {
                    branch 'origin/main'
                    expression {
                        params['RUN-TYPE'] == 'manual'
                    }
                }
            }
            steps {
                echo 'Running tests...'
                sh 'poetry run pytest'
            }
        }
    }
}