import boto3

# Boto3 will automatically use the IAM role credentials assigned to the EC2 instance
ec2 = boto3.client('ec2')

# Use Boto3 to interact with AWS services
# For example, list all EC2 instances
instances = ec2.instances.all()
for instance in instances:
    print(instance.id)
imageid = instance.id

instance_type = ec2_resource


new_instance = ec2.create_instances(
    ImageId=print(imageid),
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)
print(new_instance[0].id)