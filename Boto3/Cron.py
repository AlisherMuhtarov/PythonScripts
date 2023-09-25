import boto3
import datetime
import pytz
import time

# Replace with your desired AWS region
aws_region = 'us-east-1'

# Set the desired timezone
desired_timezone = pytz.timezone('America/Chicago')

# Compute the launch time in UTC
desired_launch_time = datetime.datetime.now(desired_timezone)
desired_launch_time_utc = desired_launch_time.astimezone(pytz.utc)
time_difference_seconds = (desired_launch_time_utc - datetime.datetime.now(pytz.utc)).total_seconds()

# If the desired launch time is in the future, sleep until then
if time_difference_seconds > 0:
    print(f'Sleeping for {time_difference_seconds} seconds until the desired launch time...')
    time.sleep(time_difference_seconds)

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
