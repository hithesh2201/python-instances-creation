import os
import boto3

# Retrieve AWS credentials from environment variables
aws_access_key_id = 'AKIATM5H4H353VNATH4U'
aws_secret_access_key = '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'
region = 'us-east-1'  # Default to us-east-1 if not specified

# Check if AWS credentials are set
if aws_access_key_id is None or aws_secret_access_key is None:
    raise ValueError("AWS credentials not set. Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.")

# Create an EC2 resource
ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)

# Specify the instance IDs you want to stop
instance_ids_to_stop = ['i-01c086edfcd1980f0']  # Replace with the actual instance IDs

# Stop instances
response = ec2.instances.filter(InstanceIds=instance_ids_to_stop).stop() #.terminate() if u replace with this word it is going to terminate the instance , .start() to restart the stopped instance.

# Print the status of the instances after attempting to stop them
for state_info in response:
    print(state_info)