# AWS CodeCommit Repository Setup

## 1. Repository Overview

The project uses AWS CodeCommit as its primary source control repository.

| Configuration | Value |
|---|---|
| Repository name | aws-devops-ci-project |
| AWS Region | eu-west-2 |
| Default branch | main |
| Repository description | AWS CI pipeline using CodeCommit, CodeBuild and CodePipeline |

## 2. Repository URLs

HTTPS clone URL:

https://git-codecommit.eu-west-2.amazonaws.com/v1/repos/aws-devops-ci-project

SSH clone URL:

ssh://git-codecommit.eu-west-2.amazonaws.com/v1/repos/aws-devops-ci-project

GitHub mirror:

git@github.com:mathjken/aws-devops-ci-project.git

The AWS CodeCommit repository remains the source repository for the CI/CD pipeline. GitHub is maintained as a submission mirror.

## 3. Cloning the Repository

Clone the AWS CodeCommit repository using:

    git clone https://git-codecommit.eu-west-2.amazonaws.com/v1/repos/aws-devops-ci-project

The AWS CLI profile `aws-devops` provides authentication through IAM Identity Center.

## 4. Branching Strategy

The project uses a simple feature-branch workflow.

- main: The primary integration branch containing stable project code.
- feature branches: Used for individual enhancements and changes.
- Pull requests: Used to review changes before merging them into main.

Example feature branch:

    git checkout -b feature/s3-deployment

Check the active branch:

    git branch

## 5. Feature Branch Workflow

The development workflow is:

1. Start from the latest main branch.
2. Create a feature branch.
3. Implement and test the changes.
4. Stage and commit the changes.
5. Push the feature branch to CodeCommit.
6. Create a pull request targeting main.
7. Review and merge the pull request.
8. Verify the updated main branch.
9. Confirm that the CodePipeline execution completes successfully.

Example commands:

    git checkout main
    git pull origin main
    git checkout -b feature/s3-deployment

After making changes:

    git add .
    git commit -m "Add S3 deployment configuration"
    git push -u origin feature/s3-deployment

Pull requests are created through the AWS CodeCommit console.

## 6. Commit Message Convention

Commit messages should describe the change clearly.

Examples:

- Add AWS environment setup documentation
- Add CodeBuild post-build packaging phase
- Configure S3 deployment stage
- Add feature branch workflow evidence

## 7. CI/CD Integration

The AWS CodePipeline source stage monitors:

- Repository: aws-devops-ci-project
- Branch: main
- Source provider: AWS CodeCommit

Changes merged into main trigger the pipeline automatically through the configured source-change event integration.

## 8. Repository Verification

To inspect configured Git remotes:

    git remote -v

To inspect local branches:

    git branch -a

To inspect recent commits:

    git log --oneline

The AWS CodeCommit remote is named `origin`. The GitHub mirror is named `github`.
