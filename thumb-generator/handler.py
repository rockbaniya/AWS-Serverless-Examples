import json
import boto3
from PIL import Image
from io import BytesIO
import urllib.parse

s3 = boto3.client('s3')

def hello(event, context):
    print(f'test')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    print(key)
    
    filetype = key.split('.')[-1]
    if (key.endswith("_thumb." + filetype)):
        print(f'Not Resized')
        return 'not resized'
    return image_resize(s3_getImg(bucket, key), bucket, key, filetype)
    #return response

def s3_getImg(bucket, key):
    img = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
    return  BytesIO(img)
    
def image_resize(img, bucket, key, filetype):
    image = Image.open(img)
    new_image = image.resize((256, 256))
    
    img = BytesIO()
    new_image.save(img, 'png')
    img.seek(0)
    
    key_split = key.rsplit('.', 1)
    key = key_split[0] + '_thumb.' + filetype
    
    response = s3.put_object(
        ACL='public-read',
        Body=img,
        Bucket=bucket,
        ContentType='image/' + filetype,
        Key=key
    )
    return response
