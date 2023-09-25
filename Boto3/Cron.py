import boto3
import datetime
import pytz

# Replace with your desired AWS region
aws_region = 'us-east-1'

# Set the desired timezone
desired_timezone = pytz.timezone('America/Chicago')

# Compute the launch time in UTC
desired_launch_time = datetime.datetime.now(desired_timezone)
desired_launch_time_utc = desired_launch_time.astimezone(pytz.utc)

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region)

# Create an EC2 instance 
instance = ec2.run_instances(
    ImageId='ami-03a6eaae9938c858c', 
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='laptop_key',  # Replace with your EC2 key pair name
)

print('Instance created with InstanceId:', instance['Instances'][0]['InstanceId'])
print('Scheduled launch time:', desired_launch_time_utc)
