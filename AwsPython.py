import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances()
# Retrieve all images
response = ec2_client.describe_images(Owners=['self'])

# Extract image IDs
image_ids = [image['ImageId'] for image in response['Images']]

# Print image IDs
for image_id in image_ids:
    print(image_id)


