import boto3

#Can refer to any s3 inside our Amazon account using the s3 var
s3 = boto3.client('s3')

s3.upload_file(
    Filename='/home/ec2-user/environment/AWS_Automation_Boto3/HTML-Codecademy.pdf', 
    Bucket='aslowinski-11082022', 
    Key='html.pdf'
    )