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
        // stage('branch_debug') {
        //     steps {
        //         echo "GIT_BRANCH: ${env.GIT_BRANCH}"
        //         echo "BRANCH_NAME: ${env.BRANCH_NAME}"
        //     }
        // }
        stage('pull_code') {
            when {
                anyOf {
                    expression { 
                        env.GIT_BRANCH == 'origin/main' 
                    }
                    expression { 
                        params['RUN-TYPE'] == 'manual' 
                    }
                }
            }   
            steps {
                echo 'Pulling code...'
                git credentialsId: 'SSH_YP_AutoTests_Sprint_3', 
                    url: 'git@github-yp_autotests_sprint_3:PaulNero/YP_AutoTests_Sprint_3.git',
                    branch: 'main'
            }
        }
        stage('prepare_environment') {
            when {
                anyOf {
                    expression { 
                        env.GIT_BRANCH == 'origin/main' 
                    }
                    expression { 
                        params['RUN-TYPE'] == 'manual'
                    }
                }
            }
            steps {
                echo 'Preparing environment...'
                withCredentials([
                    string(credentialsId: 'NAME', variable: 'NAME'),
                    string(credentialsId: 'PASSWORD_RIGHT', variable: 'PASSWORD_RIGHT'),
                    string(credentialsId: 'PASSWORD_6_SYMBOLS', variable: 'PASSWORD_6_SYMBOLS'),
                    string(credentialsId: 'PASSWORD_WRONG', variable: 'PASSWORD_WRONG'),
                    string(credentialsId: 'DELAY', variable: 'DELAY'),
                    string(credentialsId: 'EMAIL_FOR_LOGIN', variable: 'EMAIL_FOR_LOGIN'),
                    string(credentialsId: 'MAIN_LINK', variable: 'MAIN_LINK')
                ]) {
                    sh '''
                        cat > .env << EOF
NAME=${NAME}
PASSWORD_RIGHT=${PASSWORD_RIGHT}
PASSWORD_6_SYMBOLS=${PASSWORD_6_SYMBOLS}
PASSWORD_WRONG=${PASSWORD_WRONG}
DELAY=${DELAY}
EMAIL_FOR_LOGIN=${EMAIL_FOR_LOGIN}
MAIN_LINK=${MAIN_LINK}
EOF
                        chmod 600 .env
                    '''
                }
            }
        }
        stage('install_dependencies') {
            when {
                anyOf {
                    expression { 
                        env.GIT_BRANCH == 'origin/main' 
                    }
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
                    expression { 
                        env.GIT_BRANCH == 'origin/main' 
                    }
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