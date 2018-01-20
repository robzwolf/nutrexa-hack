# This file is the new ReadFromDatabase.js

from __future__ import print_function
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def get_item_information(food_item):
    # Get item information
    print("get_item_information called", food_item)
    return true
