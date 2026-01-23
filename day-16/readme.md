 Day 15 – IAM User with Least Privilege

Objective
Create an AWS IAM user following the **Principle of Least Privilege** — only the minimum permissions required.

Steps Taken
1. Created a new IAM user in AWS.
2. Created a custom policy allowing only `s3:ListAllMyBuckets`.
3. Attached the policy directly to the user.

Policy Effect
- ✅ Can list S3 buckets  
- ❌ Cannot access other AWS services or modify anything  

Verification
- `aws s3 ls` works  
- Other services return **AccessDenied**

Skills Demonstrated
- AWS IAM fundamentals  
- Least Privilege principle  
- Policy creation and attachment  
