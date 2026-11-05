# AWS Environment Setup

## 1. Project Overview

This document describes the AWS environment used for the AWS DevOps CI/CD project.

The project uses AWS CodeCommit, CodeBuild and CodePipeline to automate source control, application testing and deployment.

## 2. AWS Environment Details

| Configuration | Value |
|---|---|
| AWS Account ID | 672417491335 |
| AWS Region | eu-west-2 (London) |
| AWS CLI Profile | aws-devops |
| Authentication | AWS IAM Identity Center (SSO) |
| Permission Set | AdministratorAccess |
| Session Identity | uzoma-admin |

## 3. Prerequisites

The following tools are required:

- AWS CLI version 2
- Git
- Python 3.12
- pip
- Visual Studio Code or another code editor
- WSL2 with Ubuntu (for the local development environment)

Check the AWS CLI installation:

    aws --version

Check the Git installation:

    git --version

Check the Python installation:

    python3 --version

## 4. AWS CLI Configuration

The project uses AWS IAM Identity Center for authentication rather than storing long-term AWS access keys.

The AWS CLI profile is named `aws-devops`.

The profile is configured with:

- SSO session: aws-devops-session
- SSO start URL: https://d-9c67b76f96.awsapps.com/start
- SSO region: eu-west-2
- Default AWS region: eu-west-2
- Output format: json

To authenticate, run:

    aws sso login --profile aws-devops --use-device-code

This opens the device authorisation process. Complete the authentication using the browser.

## 5. Verify AWS Credentials

After authentication, verify the active AWS identity:

    aws sts get-caller-identity --profile aws-devops

Successful verification returns:

- UserId
- Account
- Arn

The project was successfully verified against AWS account `672417491335`, using the `AdministratorAccess` permission set through an assumed IAM Identity Center role.

To inspect the active CLI configuration:

    aws configure list --profile aws-devops

To confirm the configured region:

    aws configure get region --profile aws-devops

## 6. AWS Services Used

| AWS Service | Purpose |
|---|---|
| AWS IAM | Identity and access management |
| AWS CodeCommit | Git source code repository |
| AWS CodeBuild | Application build and automated testing |
| AWS CodePipeline | CI/CD workflow orchestration |
| Amazon S3 | Pipeline artifact storage and application deployment |
| Amazon CloudWatch | Build logs and monitoring |
| Amazon EventBridge | Automatic pipeline execution following source changes |

## 7. Project Resources

| Resource | Name |
|---|---|
| CodeCommit repository | aws-devops-ci-project |
| CodeBuild project | aws-devops-ci-build |
| CodePipeline | aws-devops-ci-pipeline |
| AWS Region | eu-west-2 |

## 8. Security Considerations

- AWS authentication uses IAM Identity Center.
- No permanent AWS access keys are stored in the project repository.
- IAM service roles are used by CodeBuild and CodePipeline.
- Credentials, tokens and other sensitive information must not be committed to Git.
- The local Python virtual environment and environment files are excluded through `.gitignore`.

## 9. Verification

The AWS CLI identity verification was successfully completed using:

    aws sts get-caller-identity --profile aws-devops

The AWS account, authenticated session and assumed IAM role were returned successfully.

Additional verification evidence is stored in the project's evidence directory.


## 10. IAM Service Roles and Permissions

The project uses dedicated IAM service roles to grant CodeBuild and CodePipeline the permissions required to execute the CI/CD workflow.

### CodeBuild Service Role

**Role name:** `codebuild-aws-devops-ci-build-service-role`

**Attached customer-managed policy:**
- `CodeBuildBasePolicy-aws-devops-ci-build-eu-west-2`

This policy provides the permissions required by the CodeBuild project to perform its build operations and interact with the configured build resources.

### CodePipeline Service Role

**Role name:** `AWSCodePipelineServiceRole-eu-west-2-aws-devops-ci-pipeline`

**Attached customer-managed policies:**
- `CodePipeline-CodeCommit-eu-west-2-aws-devops-ci-pipeline`
- `AWSCodePipelineServiceRole-eu-west-2-aws-devops-ci-pipeline`
- `CodePipeline-CodeBuild-eu-west-2-aws-devops-ci-pipeline`

These policies support the pipeline's integration with CodeCommit and CodeBuild and its orchestration activities.

**Additional inline policy:** `CodePipelineS3DeploymentAccess`

This custom policy grants the pipeline access to the dedicated S3 deployment bucket:

`aws-devops-ci-deployment-672417491335-20261105`

The permissions include:

| Resource | Actions |
|---|---|
| S3 deployment bucket | `s3:GetBucketVersioning`, `s3:GetBucketAcl`, `s3:GetBucketLocation`, `s3:ListBucket` |
| Objects in deployment bucket | `s3:PutObject`, `s3:PutObjectAcl`, `s3:GetObject`, `s3:GetObjectVersion` |

These permissions allow CodePipeline to inspect the deployment bucket and upload or retrieve deployment artifacts.

The deployment bucket has versioning enabled and all four S3 Block Public Access settings enabled.
