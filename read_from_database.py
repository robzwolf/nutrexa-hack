# This file is the new ReadFromDatabase.js

from __future__ import print_function
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def get_item_information(food_item):
    # Get item information

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Items')

	try:
	    response = table.get_item(
	        Key={
	            'Identifier': food_item[0]
	        }
	    )
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    item = response['Item']
	    print("GetItem succeeded:")
	    print(json.dumps(item, indent=4, cls=DecimalEncoder))

	    print("get_item_information called", food_item)
	    return True