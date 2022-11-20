import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
for bucket in response:
    print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))