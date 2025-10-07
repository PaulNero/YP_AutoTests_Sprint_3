pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '--network host --shm-size=2g -v /var/lib/jenkins/.cache/pypoetry:/root/.cache/pypoetry'
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
        POETRY_HOME = '/root/.local'
        PATH = '/root/.local/bin:$PATH'
        PYTHONUNBUFFERED = '1'
        PIP_DISABLE_PIP_VERSION_CHECK = 'on'
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Installing system deps and Poetry...'
                sh '''
                    apt-get update -y && apt-get install -y curl build-essential libffi-dev libssl-dev git
                    pip install --no-cache-dir poetry
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing project dependencies via Poetry...'
                sh '''
                    poetry config virtualenvs.create true
                    poetry config virtualenvs.in-project true
                    poetry install --no-root -vvv
                '''
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    poetry run pytest --maxfail=3 --disable-warnings -q --junitxml=pytest-results.xml
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
            sh 'rm -rf /root/.cache/pip'
        }
    }
}
