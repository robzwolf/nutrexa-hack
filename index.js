const Alexa = require('alexa-sdk');
const post_to_database = require("PostToDatabase");
const read_from_database = require("ReadFromDatabase");

exports.handler = function(event, context, callback) {
    let alexa = Alexa.handler(event, context);

    alexa.appId = 'amzn1.ask.skill.eecf7bbd-3fd1-4b53-a552-a100f52c6aab';

    ///alexa.dynamoDBTableName = 'YourTableName'; // creates new table for session.attributes

    alexa.registerHandlers(handlers);
    alexa.execute();
};

const HELLO_MESSAGE = 'Hello World from Alexa'
const HELP_MESSAGE = 'You can say hello, or, you can say exit... What can I help you with?';
const HELP_REPROMPT = 'What can I help you with?';
const STOP_MESSAGE = 'Goodbye!';

const handlers = {
    'LaunchRequest': function () {
        this.emit('MyIntent');
    },
    'MyIntent': function () {
        const speechOutput = HELLO_MESSAGE;

        this.response.speak(speechOutput);
        this.emit(':responseReady');
    },
    'AMAZON.HelpIntent': function () {
        const speechOutput = HELP_MESSAGE;
        const reprompt = HELP_REPROMPT;

        this.response.speak(speechOutput).listen(reprompt);
        this.emit(':responseReady');
    },
    'AMAZON.CancelIntent': function () {
        this.response.speak(STOP_MESSAGE);
        this.emit(':responseReady');
    },
    'AMAZON.StopIntent': function () {
        this.response.speak(STOP_MESSAGE);
        this.emit(':responseReady');
    },
    'AddFoodIntent': function () {
        
        food_type = this.event.request.intent.slots.food_type.value;
        
        foodItem = {
            name: food_type,
            quantity: 1
        }
        
        // Check if the item is understood (in food items DB) and act appropriately
        if(!post_to_database.checkItemExistence(foodItem) === true) {
            this.response.speak("That item did not exist, adding it to the database.");
            post_to_database.addItemToDB(foodItem);
        }
        else {
            this.response.speak("That item existed already.");
        }
        
        
        // Now that we've ensured the item exists in food items DB, add it to food consumption
        //post_to_database.consumeFoodItem(foodItem);
        
        
        this.emit(':responseReady');
    },
    'GetAllFoodIntent': function () {
        // Get a list of all food from the dynamoDB
        
    }
}; 
