import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_snapshots(SnapshotIds=[
        'snap-0f0cf5c61c4296b60',])

print(response)