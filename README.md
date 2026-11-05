# AWS DevOps CI/CD Pipeline Project

## 1. Project Overview

This project demonstrates the implementation of an automated Continuous Integration (CI) pipeline using AWS CodeCommit, AWS CodeBuild, AWS CodePipeline and Amazon S3.

The pipeline retrieves source code from CodeCommit, executes automated Python tests through CodeBuild and stores pipeline artifacts in Amazon S3.

## 2. Architecture

The pipeline follows this workflow:

1. Developer pushes code to AWS CodeCommit.
2. Amazon EventBridge detects the repository change.
3. AWS CodePipeline starts automatically.
4. AWS CodeBuild installs dependencies and executes automated tests.
5. Build artifacts are stored in the pipeline's Amazon S3 artifact store.

## 3. AWS Services

| Service | Purpose |
|---|---|
| AWS CodeCommit | Source code repository |
| AWS CodeBuild | Build execution and automated testing |
| AWS CodePipeline | CI/CD workflow orchestration |
| Amazon S3 | Pipeline artifact storage |
| Amazon EventBridge | Automatic source change detection |
| AWS IAM | Access control and service permissions |
| Amazon CloudWatch | Build logs and monitoring |

## 4. Repository Structure

```text
aws-devops-ci-project/
├── app.py
├── test_app.py
├── requirements.txt
├── buildspec.yml
└── README.md


5. Application and Testing
The Python application provides a simple addition function.

Automated tests are implemented using pytest.

To install dependencies locally:
python -m pip install -r requirements.txt


To execute tests:
python -m pytest --junitxml=test-results.xml


6. CodeBuild Configuration
The build process is defined in buildspec.yml.

The configuration:
- Uses Python 3.12.
- Installs dependencies from requirements.txt.
- Executes pytest.
- Generates a JUnit XML test report.
- Defines build output artifacts.
7. IAM Roles
The project uses separate IAM service roles:
- CodeBuild service role: allows CodeBuild to perform the operations required for build execution, logging and reporting.
- CodePipeline service role: allows CodePipeline to orchestrate source and build actions and manage pipeline artifacts.
Permissions should follow the principle of least privilege.
8. Environment Variables
No custom environment variables are currently required.

The build uses the Python runtime and dependencies defined in the build configuration.
9. Pipeline Configuration
Pipeline name: aws-devops-ci-pipeline

Build project: aws-devops-ci-build

Source repository: aws-devops-ci-project

Branch: main

AWS Region: eu-west-2 (Europe London)

Pipeline type: V2

Execution mode: Queued
10. Artifact Storage
Amazon S3 is configured as the default artifact store for CodePipeline.

Pipeline artifacts are stored in the S3 bucket created for the pipeline.
11. Verification
The initial CodeBuild execution completed successfully.

The CodePipeline execution also completed successfully, with both Source and Build stages succeeding.

Further verification includes testing automatic pipeline triggering after a new commit is pushed to CodeCommit.
12. Author
AWS DevOps CI/CD learning project.

### Save the file

In Nano:

1. Press `Ctrl + O` (save).
2. Press `Enter` to confirm `README.md`.
3. Press `Ctrl + X` to exit.

Then run:

```bash
git status
