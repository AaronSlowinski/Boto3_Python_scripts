# Create a DynamoDB table for something of your choosing (e.g. movies, food, games).
# Using the Gist (https://gist.github.com/zaireali649/0ec6b90155120cf508223788b7b86efc) as a starting point, use boto3 and Python to add 10 or more items to the table.
# Use boto3 and Python to scan the DynamoDB table.

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
        TableName = 'Video_Games',
        KeySchema = [
            {
                'AttributeName' : 'Title',
                'KeyType' : 'HASH'
                
            },
            {
                'AttributeName' : 'Genre',
                'KeyType' : 'RANGE'
                
            }
            ],
            AttributeDefinitions = [
                {
                    'AttributeName' : 'Title',
                    'AttributeType' : 'S'
                    
                },
                {
                    'AttributeName' : 'Genre',
                    'AttributeType' : 'S'
                    
                }
                ],
                ProvisionedThroughput = {
                    'ReadCapacityUnits' : 10,
                    'WriteCapacityUnits' : 10
                    
                }
                
)

print("Status:", table.table_status)