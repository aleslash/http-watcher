import json
import requests
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# s3 = boto3.client('s3', endpoint_url=HOST+":4566", region_name="us-east-1", aws_access_key_id="S3_KEY", aws_secret_access_key="S3_SECRET")
s3 = boto3.client('s3')

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    logger.info('starting call with message ' + message)
    params = json.loads(message)
    content_object = s3.get_object(Bucket=params['bucket'], Key=params['object'])
    file_content = content_object['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    response = call_endpoint(json_content)
    return {'message':response}

def call_endpoint(json_data):
    logger.info('calling endpoint:{method} {uri}'.format(method=json_data['method'],uri=json_data['uri']))
    response = requests.request(json_data['method'], json_data['uri'],headers=json_data['headers'])
    logger.info('received status code {received}. expected status code {expected}'.format(received=response.status_code, expected=json_data['expected_status_code']))
    return id(response.status_code) == id(json_data['expected_status_code'])