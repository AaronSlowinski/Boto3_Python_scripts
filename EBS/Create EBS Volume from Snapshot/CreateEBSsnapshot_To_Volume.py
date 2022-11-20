import boto3

ec2 = boto3.client('ec2')

response = ec2.create_volume(
    AvailabilityZone='us-west-2a',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-0f0cf5c61c4296b60',
    VolumeType='gp2',
)

print(response)