# AWS Resource Audit Tool 

A Python automation script that audits AWS cloud resources using **Boto3 SDK** and exports a structured CSV report for governance and cost visibility.

## What It Does
- Lists all **S3 Buckets** with creation dates
- Lists all **IAM Users** with account details  
- Lists all **EC2 Instances** with type and running state
- Exports everything to a dated **CSV report**

##  Tech Stack
`Python 3` `AWS Boto3` `Amazon S3` `AWS IAM` `AWS EC2` `CSV`

##  How to Run

**1. Install dependency**
```bash
aws configure
```

**3. Run the script**
```bash
python3 aws_audit.py
```

## Sample Output
```
=============================================
     AWS RESOURCE AUDIT TOOL
=============================================
Fetching S3 buckets...
  Found: 1 bucket(s)
Fetching IAM users...
  Found: 1 user(s)
Fetching EC2 instances...
  Found: 0 instance(s)
Report saved: aws_audit_report_2026-03-05.csv
=============================================
AUDIT COMPLETE!
=============================================
```

##  Output File
Generates: `aws_audit_report_YYYY-MM-DD.csv`

| Resource Type | Name/ID | Details | Created On |
|---|---|---|---|
| S3 Bucket | mudit-audit-bucket | Object Storage | 2026-03-05 |
| IAM User | muditojha | / | 2026-03-05 |
| EC2 Instance | None found | No instances running | - |

## Author
**Mudit Ojha** — Cloud & DevOps Engineer | AZ-104 Certified  
[LinkedIn](https://linkedin.com/in/mudit-ojha) | [GitHub](https://github.com/Mudit-ojha)
