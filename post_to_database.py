# This file is the new PostToDatabase.js

from __future__ import print_function
import boto3
from random import randint
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
    print("add_item_to_DB called food items")

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



def updateOldFoodInFoodConsumptionTable(food_info):
    # Update the content for the user

    print("update_old_item_to_DB food Consumption")

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Consumption')

    userName = food_info[0]

    date = food_info[1]

    print(food_info)

    response = table.update_item(
        Key={
            'User': userName,
            'Date': date
        },
        UpdateExpression="set " +food_info[2]+ " = " +food_info[2]+ " + :quantity,  Potasium = Potasium + :valOfPotasium, Sodium = Sodium + :valOfSodium, Calories = :valOfSodium + :valOfPotasium",
        ExpressionAttributeValues={
            ':quantity' : food_info[3],
            ':valOfPotasium' : food_info[4],
            ':valOfSodium' : food_info[5]
        },
        ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    print(food_info)


def updateNewFoodInFoodConsumptionTable(food_info):
    # Update the content for the user

    print("update_new_item_to_DB food Consumption")

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Consumption')

    userName = food_info[0]

    date = food_info[1]

    print(food_info)

    response = table.update_item(
        Key={
            'User': userName,
            'Date': date
        },
        UpdateExpression="set " +food_info[2]+ " = :quantity,  Potasium = Potasium + :valOfPotasium, Sodium = Sodium + :valOfSodium",
        ExpressionAttributeValues={
            ':quantity' : food_info[3],
            ':valOfPotasium' : food_info[4],
            ':valOfSodium' : food_info[5]
        },
        ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    print(food_info)

