import boto3
import datetime
import json

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('arep')
from random import randint

def lambda_handler(event, context):
    table.put_item(Item = {
        "id":randint(0,1000000),
        "quantity":event['quantity'],
        "date":datetime.datetime.now().strftime('%m/%d/%Y')
    })
    return {
        'statusCode':201,
        'body':json.dumps('created')
    }
