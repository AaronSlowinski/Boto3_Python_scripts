import boto3
import json

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(
    TableName = 'Video_Games'
    )
    
for i in response['Items']:
    print(json.dumps(i))
