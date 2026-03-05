# aws_audit.py
# AWS Resource Audit Tool
# Banaya: Mudit Ojha
# Kya karta hai: AWS resources scan karta hai aur CSV report banata hai

import boto3          # AWS ka Python library
import csv            # CSV file banane ke liye
from datetime import datetime   # aaj ki date ke liye

# ---- FUNCTION 1: S3 Buckets fetch karo ----
def get_s3_buckets():
    print("S3 buckets fetch ho rahi hain...")
    
    # S3 service se connect karo
    s3 = boto3.client('s3')
    
    # AWS se saari buckets maango
    response = s3.list_buckets()
    
    # Sirf bucket names aur dates nikalo
    buckets = response['Buckets']
    
    print(f"Mili {len(buckets)} bucket(s)")
    return buckets

# ---- FUNCTION 2: IAM Users fetch karo ----
def get_iam_users():
    print("IAM users fetch ho rahe hain...")
    
    # IAM service se connect karo
    iam = boto3.client('iam')
    
    # AWS se saare users maango
    response = iam.list_users()
    
    users = response['Users']
    
    print(f"Mile {len(users)} user(s)")
    return users

# ---- FUNCTION 3: EC2 Instances fetch karo ----
def get_ec2_instances():
    print("EC2 instances fetch ho rahe hain...")
    
    # Mumbai region ka EC2 se connect karo
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    response = ec2.describe_instances()
    
    # EC2 response thoda alag structure mein hota hai
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    
    print(f"Mile {len(instances)} instance(s)")
    return instances

# ---- FUNCTION 4: CSV Report banao ----
def save_report(buckets, users, instances):
    # Aaj ki date se filename banao
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f"aws_audit_report_{today}.csv"
    
    print(f"Report ban rahi hai: {filename}")
    
    # CSV file kholo aur data likho
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Header row
        writer.writerow(['Resource Type', 'Name/ID', 'Details', 'Created On'])
        
        # S3 Buckets likho
        writer.writerow([])  # empty row for spacing
        writer.writerow(['--- S3 BUCKETS ---', '', '', ''])
        for bucket in buckets:
            writer.writerow([
                'S3 Bucket',
                bucket['Name'],
                'Object Storage',
                str(bucket['CreationDate'])[:10]  # sirf date, time nahi
            ])
        
        # IAM Users likho
        writer.writerow([])
        writer.writerow(['--- IAM USERS ---', '', '', ''])
        for user in users:
            writer.writerow([
                'IAM User',
                user['UserName'],
                user.get('Path', '/'),
                str(user['CreateDate'])[:10]
            ])
        
        # EC2 Instances likho
        writer.writerow([])
        writer.writerow(['--- EC2 INSTANCES ---', '', '', ''])
        if instances:
            for inst in instances:
                writer.writerow([
                    'EC2 Instance',
                    inst['InstanceId'],
                    f"{inst['InstanceType']} | {inst['State']['Name']}",
                    str(inst['LaunchTime'])[:10]
                ])
        else:
            writer.writerow(['EC2 Instance', 'None found', 
                           'No instances in ap-south-1', ''])
    
    print(f"✅ Report save ho gayi: {filename}")
    return filename

# ---- MAIN: Sab functions ek saath chalao ----
if __name__ == "__main__":
    print("=" * 50)
    print("AWS RESOURCE AUDIT TOOL")
    print("=" * 50)
    
    try:
        # Step 1: Data fetch karo
        buckets   = get_s3_buckets()
        users     = get_iam_users()
        instances = get_ec2_instances()
        
        # Step 2: Report banao
        filename = save_report(buckets, users, instances)
        
        # Step 3: Summary print karo
        print()
        print("=" * 50)
        print("AUDIT COMPLETE!")
        print(f"S3 Buckets:     {len(buckets)}")
        print(f"IAM Users:      {len(users)}")
        print(f"EC2 Instances:  {len(instances)}")
        print(f"Report saved:   {filename}")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error aaya: {e}")
        print("AWS credentials check karo — aws configure run karo")

