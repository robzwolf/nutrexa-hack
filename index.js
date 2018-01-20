const Alexa = require('alexa-sdk');
const dynamo = require("database");

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
        known_foods = ["beer", "hamburger", "apple"];
        food_type = this.event.request.intent.slots.food_type.value
        if(known_foods.indexOf(food_type) == -1) {
            // We don't know what that food item is
            // We'll add it to the DB anyway but tell the user we don't know its nutritional info
            dynamo.addToDB(food_type);
        }
        
        
        
        this.response.speak("You said you ate a " + this.event.request.intent.slots.food_type.value)
        this.emit(':responseReady');
    }
}; 
