import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

PRIVATE_BUCKET = "moku-s3-private-bucket"
PUBLIC_BUCKET = "moku-s3-public-bucket"

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']

        if source_bucket != PUBLIC_BUCKET:
            continue

        object_key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        copy_source = {
            'Bucket': source_bucket,
            'Key': object_key
        }

        # Copy object to private bucket
        s3.copy_object(
            CopySource=copy_source,
            Bucket=PRIVATE_BUCKET,
            Key=object_key
        )

        # Delete object from public bucket
        s3.delete_object(
            Bucket=source_bucket,
            Key=object_key
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Object was successfully moved!')
    }
