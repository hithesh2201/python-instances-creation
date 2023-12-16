import boto3

# Replace these variables with your values
region = 'your-aws-region'
instance_id = 'your-instance-id'
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Restart the instance
try:
    response = ec2.reboot_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} is restarting.")
except Exception as e:
    print(f"Error restarting instance: {e}")
