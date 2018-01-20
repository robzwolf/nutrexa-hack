# This file is the new PostToDatabase.js

from __future__ import print_function
import boto3

def check_item_existence(food_item):
    # Check the item exists

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Items')
    
    response = table.query(
    KeyConditionExpression=Key('Identifier').eq(food_item[0])
    )

    print("check_item_existence called", food_item[0])
    
    print(response)

    if(len(response) == 0):
        return False

    return True
    


def add_item_to_DB(food_item):
    # Add to Food_Items DB
    print("add_item_to_DB called", food_item)

    print(json.dumps(response["Item"], indent=4, cls=DecimalEncoder))
