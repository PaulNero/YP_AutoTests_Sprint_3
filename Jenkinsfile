pipeline {
    agent {
        docker {
            image 'nerobovp/npn-test-chrome-python-allure:latest'
            args '--network host --shm-size=2g -v /var/lib/jenkins/.cache/pypoetry:/home/tester/.cache/pypoetry'
        }
    }

    parameters {
        string(name: 'RUN-TYPE', defaultValue: 'auto', description: 'Type of run: auto or manual')
        string(name: 'TEST-MARKER', defaultValue: '', description: 'Run tests for a pytest mark (leave empty to run all)\n * registration: All tests for registration.\n * login: All tests for login.\n * enter_to_cabinet: All tests for enter to cabinet\n * open_constructor: All tests for open constructor after cabinet\n * exit: All tests for exit from cabinet \n * constructor_change: All tests for change parts of constructor')
    }

    triggers {
        githubPush()
        // Пока отключен так как сайт недоступен
        // Проверка: https://downforeveryoneorjustme.com/stellarburgers.nomoreparties.site

        // минуты, часы, день месяца, месяц, день недели
        //pollSCM('0 3 * * *')
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
                script {
                    def pytestCmd = "poetry run pytest --maxfail=3 --disable-warnings -q --junitxml=pytest-results.xml"
                    
                    if (params.TEST_MARKER?.trim()) {
                        pytestCmd += " -m ${params.TEST_MARKER}"
                    }
                    
                    sh pytestCmd
                }
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
