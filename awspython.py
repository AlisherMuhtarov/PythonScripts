import boto3

# Boto3 will automatically use the IAM role credentials assigned to the EC2 instance
ec2 = boto3.resource('ec2')

# Use Boto3 to interact with AWS services
# For example, list all EC2 instances
instances = ec2.instances.all()
for instance in instances:
    print(instance.id)
imageid = instance.id
print(imageid)
