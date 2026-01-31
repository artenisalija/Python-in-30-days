## Day 24 - Lambda Function

1. Created Simple CRUD app with Mangum to wrap it inside
2. Created IAM user with permissions 
    1. AmazonEC2ContainerRegistryFullAccess 
    2. AWSLambda_FullAccess
    3. IAMFullAccess
    4. IAMReadOnlyAccess
3. Downloaded AWSCLI2 in my system
4. Created a docker file
5. Signed in using IAM user 
6. Created ECR repository
7. Started AWS configure using Push Commands from ECR
8. Finished the Docker Image push into the ecr
9. Created AWS Lambda Function from container registry
10. Ran a test to see if the function works properly
11. Open the Function URL and everything works fine

```cmd
- aws aws configure

- aws ecr get-login-password --region eu-north-1 | docker login --aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com

- docker build --platform linux/amd64 --provenance=false -t <local-image-name> .

- docker push <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/<repo-name>:latest

- docker push 606222243775.dkr.ecr.eu-north-1.amazonaws.com/day-24-lambda-function:latest