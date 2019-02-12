import json
import boto3

db = boto3.client('dynamodb')

def create(event, context):
    data = (event['body'])
    print(f'{data}')

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }