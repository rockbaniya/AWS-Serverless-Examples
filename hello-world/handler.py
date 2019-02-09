import json
import os
import boto3


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    print(os.environ['var1'])
    #client = boto3.client('lambda')
    return response
