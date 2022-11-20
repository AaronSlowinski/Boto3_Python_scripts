import boto3

s3 = boto3.client('s3')

response = s3.list_objects(
    Bucket='aslowinski-11082022')
    
print (response)