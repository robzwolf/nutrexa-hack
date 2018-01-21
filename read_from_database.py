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
                'Date': '20180121'
            }
            #ConditionExpression={'attribute_exists(foodType)'}
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        print("Returning: 0")
        return 0
    else:
        item = response['Item']
        print(item)
        print("GetItem with Food Type succeeded:")
        #return item
        print("Returning: ", item[foodType])
        return item[foodType]


def get_user_information_for_NutritionType(nutritional_category):
    # Get nutritional information for a specific nutritional_category (i.e. sodium or potassium)

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
        print("error getting user information for nutrition type: " + nutritional_category)
    else:
        item = response['Item']
        print(item)
        print("Get user information for nutrition type succeeded")
        print("Returning: " + nutritional_category)
        if nutritional_category == "sodium":
            print("Returning: ", item["Sodium"])
            return item["Sodium"]
        elif nutritional_category == "potassium":
            print("Returning: ", item["Potasium"])
            return item["Potasium"]
        elif nutritional_category == "calories":
            print("Returning: ", item["Calories"])
            return item["Calories"]
        else:
            print("Returning -1 because nutritional_category was neither sodium nor potassium")
            return -1
