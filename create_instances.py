import boto3

# AWS credentials and region
aws_access_key_id = 'AKIATM5H4H353VNATH4U' 
aws_secret_access_key = '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'
region = 'us-east-1'

# Create an EC2 resource
ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)

# Define instance parameters
instance_params = {
    'ImageId': 'ami-018ba43095ff50d08',  # Replace with the desired AMI ID
    'InstanceType': 't2.micro',  # Replace with the desired instance type
    'MinCount': 1,
    'MaxCount': 1,  # Number of instances to launch
    'KeyName' : 'demokey',
    'SecurityGroups' : ['allow-all']
}

# Launch instances
instances = ec2.create_instances(**instance_params)

# Print instance IDs
for instance in instances:
    print(f"Launched instance: {instance.id}")
