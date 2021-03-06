"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import boto3
import post_to_database
import read_from_database
import datetime
import nutritionix_api_key
import nutritionix

# Recommended daily allowances in milligrams
POTASSIUM_RDA = 3500
SODIUM_RDA    = 2400

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        # ,
        # 'card': {
        #     'type': 'Simple',
        #     'title': "SessionSpeechlet - " + title,
        #     'content': "SessionSpeechlet - " + output
        # },
        # 'reprompt': {
        #     'outputSpeech': {
        #         'type': 'PlainText',
        #         'text': reprompt_text
        #     }
        # }
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your favorite color by saying, " \
                    "my favorite color is red."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_get_nutrition_intent(intent):

    nutritional_category = None
    try:
        nutritional_category = intent['slots']['nutritional_category']['value'].lower()
    except:
        pass

    food_type = None
    try:
        food_type = intent['slots']['food_List']['value'].lower()
    except:
        pass
    
    #if(!nutritional_category=null && !food_type=null):

    if nutritional_category is None and food_type is None:
        result = read_from_database.get_user_information() # If the user asked "how healthy am I today"
        sodiumContent = result['Sodium']
        print(sodiumContent)
        potasiumContent = result['Potasium']
        print(potasiumContent)
        caloriesContent = result['Calories']
        print(potasiumContent)
        speech_output = ""
        if sodiumContent > 5000:
            print("Lower your sodium Content")
            speech_output += "You've eaten too much sodium today. The limit is 1000 and you've had " + str(sodiumContent) + ". "
        if potasiumContent > 10000:
            print("Lower your potasiumContent")
            speech_output += "You've eaten too much potassium today. The limit is 500 and you've had " + str(potasiumContent) + ". "
        if caloriesContent > 5000:
            print("Lower your caloriesContent")
            speech_output += "You've eaten too much today. Your calories intake for today is " + str(caloriesContent) + ". "
        if speech_output == "":
            print("You are in good health")
            speech_output = "Congratulations, you are in great health!"    
        return basic_say(speech_output)
        
    elif nutritional_category is None and food_type is not None:
        # User asked "How many food_type did I have today"
        #print(food_type)
        result = read_from_database.get_user_information_for_FoodType(food_type)
        return basic_say("You have eaten " + str(result) + " " + str(food_type) + " today")
    if not nutritional_category is None and food_type is None:
        # User asked "What's my nutritional_category level"
        result = read_from_database.get_user_information_for_NutritionType(nutritional_category)
        if result == -1:
            return basic_say("Sorry, I don't know what " + nutritional_category + " means")
        return basic_say("You've eaten " + str(result) + " " + nutritional_category + " today")
        
    result = read_from_database.get_user_information()
    print(result)

def handle_add_food_intent(intent):
    
    
    
    user_food = intent['slots']['food_type']['value'].lower()
    
    #nutritionix.do_nutri(user_food)
    
    # Default quantity is 1 if it was not specified
    quantity = 1
    try:
        if intent['slots']['food_quantity']['value'] != '?':
            quantity = intent['slots']['food_quantity']['value']
    except:
        pass
    
    food_item = [user_food, int(quantity)]
    
    print("Food item is", food_item)
    
    itemExistance = post_to_database.check_item_existence(food_item)
    
    # Check if the item is understood (exists in Food_Items DB) and act appropriately
    if itemExistance:
        print("check_item_existence returned True")
        #return basic_say("That item existed already.")
    else:
        print("check_item_existence returned False")
        post_to_database.add_item_to_DB(food_item)
        #return basic_say("That item did not exist, adding it to Food Items database.")
    
    # Get current date
    now = datetime.datetime.now()
    
    # Get food item information (sodium, potassium etc.)
    item_info = read_from_database.get_item_information([user_food])
    
    # Set username
    username = "Amish"
    
    # Make a pretty date string yyyymmdd
    #date_string = str(now.year) + str(now.month) + str(now.day)
    date_string = "20180121" # Hardcoded because of leading zero on month 
    
    # Get potassium
    potassium = item_info['Potasium']
    
    # Get sodium
    sodium = item_info['Sodium']
    
    # Get Calories
    calories = item_info['Calories']
    
    # Prepare data in format accepted by post_to_database
    data_to_post = [username, date_string, user_food, int(quantity), potassium, sodium, calories]
    
    # Send data block to database and calculate new totals for the day
    if itemExistance:
        post_to_database.updateOldFoodInFoodConsumptionTable(data_to_post)
    else:
        post_to_database.updateNewFoodInFoodConsumptionTable(data_to_post)
    
    return basic_say("Okay cool, I hope you enjoyed your %s!" % user_food)
    

def handle_list_all_intent(intent):
    print("Called handle_list_all_intent with intent:", intent)
    all_user_info = read_from_database.get_user_information()
    print("all_user_info:", all_user_info)
    
    skip_keys = ["Date", "Sodium", "User", "Calories", "Potasium"]
    consumed_food_items = {}
    for key in all_user_info.keys():
        if key not in skip_keys:
            consumed_food_items[key] = all_user_info[key]
    print("consumed_food_items:", consumed_food_items)
    speech_output = "You have eaten "
    
    for food in consumed_food_items.keys():
        speech_output += str(consumed_food_items[food]) + " " + food + ", "
    
    speech_output += ". Mmmm, delicious. Looks like someone was hungry today!"
    print("speech_output:", speech_output)
    return basic_say(speech_output)
    
    """ Date
    hambyrger
    Sodium 
    bagel
    cheeseandwich
    User
    Calories
    Potasium"""


def basic_say(words, should_end_session=True):
    return build_response({}, build_speechlet_response(
        "Response", words, None, should_end_session))

def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_color_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyColorIsIntent":
        return set_color_in_session(intent, session)
    elif intent_name == "WhatsMyColorIntent":
        return get_color_from_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "AddFoodIntent":
        return handle_add_food_intent(intent)
    elif intent_name == "GetNutritionIntent":
        return handle_get_nutrition_intent(intent)
    elif intent_name == "ListAllIntent":
        print("called ListAllIntent")
        return handle_list_all_intent(intent)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def mytempfunction(event):
    # client = boto3.client('dynamodb')
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Food_Items')
    response = table.get_item(
        Key={
            'Identifier': 'Hamburger'
        }
    )
    print(json.dumps(response["Item"], indent=4, cls=DecimalEncoder))

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    """print(event)
    if("key1" in event):
        return mytempfunction(event)"""
        
    """print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])"""

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
    
