import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
    InstanceIds=[
        'i-0b95f7702e22cabce',
        'i-07ac27d86bf01299b',
        'i-0fd514c93fdace021'
        
        
    ],
)

print(response)