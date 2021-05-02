import json
import requests
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# s3 = boto3.client('s3', endpoint_url=HOST+":4566", region_name="us-east-1")
# sns = boto3.client('sns', endpoint_url=HOST+":4566", region_name="us-east-1")
s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    logger.info('reading bucket {bucket}'.format(bucket=event['bucket']))
    files_contents = s3.list_objects_v2(Bucket=event['bucket'])['Contents']
    files = []
    for file in files_contents:
        message = {'bucket':event['bucket'],'object':file['Key']}
        files.append(json.dumps(message))
        sns.publish(TopicArn=event['topicSNSArn'], Message=json.dumps(message))
        logger.info('message {message}'.format(message=json.dumps(message)))
    print(files)
    return {'message':files}