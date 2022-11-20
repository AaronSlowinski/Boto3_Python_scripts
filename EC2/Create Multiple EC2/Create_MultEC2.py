import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(ImageId='ami-094125af156557ca2', 
    InstanceType='t2.micro', 
    MaxCount=3, 
    MinCount=3
  )

print(instance)