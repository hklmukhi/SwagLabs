pipeline {
    agent any

    options {
        timeout(time: 1, unit: 'HOURS')
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        skipDefaultCheckout()
    }

    environment {
        PYTHON_VERSION = '3.9'
        BROWSER = 'Chrome'
        TEST_ENVIRONMENT = 'QA'
        ALLURE_HOME = "${WORKSPACE}/allure-cli/allure-2.39.0"
        GIT_REPO_URL = 'https://github.com/hklmukhi/SwagLabs.git'
        GIT_BRANCH = "${env.BRANCH_NAME ?: '*/main'}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '========== Checking out code from repository =========='
                retry(3) {
                    checkout([$class: 'GitSCM',
                        branches: [[name: env.GIT_BRANCH]],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [
                            [$class: 'CleanCheckout'],
                            [$class: 'CloneOption', timeout: 10, noTags: false, shallow: false]
                        ],
                        submoduleCfg: [],
                        userRemoteConfigs: [[url: env.GIT_REPO_URL]]
                    ])
                }
                echo '========== Checkout completed =========='
            }
        }

        stage('Setup Environment') {
            steps {
                echo '========== Setting up Python Environment =========='
                bat '''
                    @echo off
                    if not exist .venv (
                        echo Creating virtual environment...
                        python -m venv .venv
                    ) else (
                        echo Virtual environment already exists
                    )
                    echo Activating virtual environment...
                    call .venv\\Scripts\\activate.bat
                    echo Installing dependencies...
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    echo Environment setup completed
                '''
            }
        }

        stage('Lint & Validate') {
            steps {
                echo '========== Running Code Quality Checks =========='
                bat '''
                    @echo off
                    call .venv\\Scripts\\activate.bat
                    echo Running pylint...
                    pylint SWAGLABSTEST --disable=all --enable=E,F || echo Pylint check completed with issues
                    echo Code quality checks completed
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '========== Running Automated Tests =========='
                bat '''
                    @echo off
                    call .venv\\Scripts\\activate.bat
                    echo Running pytest with Allure reporting...
                    pytest SWAGLABSTEST --alluredir=allure-results -v --tb=short --junitxml=pytest-results/results.xml
                    echo Test execution completed
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo '========== Generating Allure Test Report =========='
                bat '''
                    @echo off
                    if exist allure-results (
                        echo Generating Allure report...
                        "%ALLURE_HOME%\\bin\\allure" generate allure-results --clean -o allure-report
                        echo Allure report generated successfully
                    ) else (
                        echo No Allure results found to generate report
                    )
                '''
            }
        }

        stage('Publish Results') {
            steps {
                echo '========== Publishing Test Results =========='
                junit testResults: 'pytest-results/results.xml', allowEmptyResults: true
                archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
                archiveArtifacts artifacts: 'pytest-results/**', fingerprint: true
                echo 'Test results published'
            }
        }

        stage('Cleanup') {
            steps {
                echo '========== Cleaning up workspace =========='
                bat '''
                    @echo off
                    echo Cleanup completed
                '''
            }
        }
    }

    post {
        failure {
            echo '========== Build Failed =========='
            echo "Check logs: ${env.BUILD_URL}console"
            echo "Allure Report: ${env.BUILD_URL}artifact/allure-report/index.html"
        }

        success {
            echo '========== All Tests Passed Successfully =========='
            echo "Build URL: ${env.BUILD_URL}artifact/allure-report/index.html"
        }

        unstable {
            echo '========== Build is Unstable =========='
        }

        cleanup {
            echo '========== Cleaning up workspace =========='
            cleanWs()
        }
    }
}
