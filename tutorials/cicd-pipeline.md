# CI/CD Pipeline

TL;DR
- Set up an automated pipeline to build, test, and deploy code using AWS CodePipeline or GitHub Actions.
- Use CodeBuild for builds/tests and CodeDeploy or CloudFormation for deployment.
- Keep builds reproducible with container images or buildspec files.
- Run unit tests and security scans early in the pipeline.
- Start with a simple pipeline and add stages incrementally.
- Use IAM least-privilege for pipeline roles.

Prerequisites
- Source repo (GitHub, CodeCommit) and AWS CLI configured.
- IAM roles for CodePipeline/CodeBuild with required permissions.
- Buildspec.yml in repo for CodeBuild.

Steps
1. Add a `buildspec.yml` to repo with build/test steps.
2. Create a CodeBuild project:
```
aws codebuild create-project --name my-build --source type=GITHUB,location=https://github.com/owner/repo --environment computeType=BUILD_GENERAL1_SMALL,image=aws/codebuild/standard:6.0
```
3. Create an S3 bucket for pipeline artifacts:
```
aws s3 mb s3://my-pipeline-artifacts
```
4. Create a CodePipeline pipeline that pulls from source, uses CodeBuild, and deploys (CloudFormation/CodeDeploy).
5. Configure deployment stage (CloudFormation or ECS/Elastic Beanstalk) and test with a commit.
6. Add test/reporting stages and notifications for failures.

Cost notes
- Charged for CodeBuild minutes, CodePipeline active pipelines, and artifact storage in S3. Keep builds efficient.

Quick troubleshooting
- Pipeline stuck: check IAM permissions and event history in CloudWatch.
- Build failures: review build logs in CodeBuild and re-run locally.
- Deployment rollback: inspect CloudFormation events or CodeDeploy logs.

Checklist
- `buildspec.yml` present and tested locally.
- Pipeline has source, build, and deploy stages.
- Roles and artifact bucket permissions configured.
# Tutorials

AWS Tutorials service