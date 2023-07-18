import boto3

def lambda_handler(event, context):
    # Retrieve existing instance information
    existing_instance_id = 'i-09faaf208a46f175d'  # Replace 'your-existing-instance-id' with the actual existing instance ID'

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(InstanceIds=[existing_instance_id])
    reservations = response['Reservations']
    existing_instance = reservations[0]['Instances'][0]

    existing_image_id = existing_instance['ImageId']
    existing_instance_type = existing_instance['InstanceType']

    # Create a new EC2 instance using the retrieved information
    ec2_resource = boto3.resource('ec2')

    new_instance = ec2_resource.create_instances(
        ImageId=existing_image_id,
        InstanceType=existing_instance_type,
        MinCount=1,
        MaxCount=1
    )

    # Print the new instance ID
    new_instance_id = new_instance[0].id
    print("New Instance ID:", new_instance_id)

    response = {
        'statusCode': 200,
        'body': f'New Instance Created: {new_instance_id}'
    }
    
    return response
