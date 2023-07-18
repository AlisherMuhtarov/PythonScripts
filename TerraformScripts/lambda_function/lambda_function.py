import boto3

def lambda_handler(event, context):
    # Retrieve existing instance information
    existing_instance_id = 'i-0a0081919bf907032'  # Replace 'your-existing-instance-id' with the actual existing instance ID'

    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Describe the existing instances
    response = ec2_client.describe_instances(InstanceIds=[existing_instance_id])
    existing_instance = ['Instances'][0]

    # Extract necessary information from the existing instance
    existing_image_id = existing_instance['ImageId']
    existing_instance_type = existing_instance['InstanceType']

    # Create an EC2 resource
    ec2_resource = boto3.resource('ec2')

    # Create a new EC2 instance using the retrieved information
    new_instance = ec2_resource.create_instances(
        ImageId=existing_image_id,
        InstanceType=existing_instance_type,
        MinCount=1,
        MaxCount=1
    )

    # Print the new instance ID
    new_instance_id = new_instance[0].id
    print("New Instance ID:", new_instance_id)

    # Create a response dictionary
    response = {
        'statusCode': 200,
        'body': f'New Instance Created: {new_instance_id}'
    }
    
    return response