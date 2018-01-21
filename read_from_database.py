# This file is the new ReadFromDatabase.js

from __future__ import print_function
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

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
        return item



def get_user_information():
    #Get all information and check the health

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Consumption')

    try:
        response = table.get_item(
            Key={
                'User': 'Amish',
                'Date': '20180121'
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        return item


def get_user_information_for_FoodType(foodType):
    #Get information of the particular food and check the quantity

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Consumption')

    try:
        response = table.get_item(
            Key={
                'User': 'Amish',
            },
            ConditionExpression={'attribute_exists(foodType)'}
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem with Food Type succeeded:")
        return item


def get_user_information_for_NutritionType():
    #Get all information and check the health

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Consumption')