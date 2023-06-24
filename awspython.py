import boto3

ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')

image_id = instance.image_id
print(image_id)
