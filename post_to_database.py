# This file is the new PostToDatabase.js

from __future__ import print_function
import boto3
import random
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def check_item_existence(food_item):
    # Check the item exists

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Items')
    
    response = table.query(
    KeyConditionExpression=Key('Identifier').eq(food_item[0])
    )

    print("check_item_existence called", food_item[0])

    if(len(response['Items']) == 0):
        return False

    return True
    


def add_item_to_DB(food_item):
    # Add to Food_Items DB
    print("add_item_to_DB called", food_item[0])

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Items')

    response = table.put_item(
       Item={
            'Identifier': food_item[0],
            'Sodium': randint(20,100),
            'Potasium': randint(120,180)
            }
    )

    print("PutItem succeeded:")
