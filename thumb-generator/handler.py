import json
import boto3
from PIL import _imaging
from PIL import Image

s3 = boto3.client('s3')

def hello(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    return s3_getImg(bucket, key)['LastModified']
    return event

def s3_getImg(bucket, key):
    return  (s3.get_object(Bucket=bucket, Key=key))