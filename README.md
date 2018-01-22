# Nutrexa
Alexa Skill developed at Hack Cambridge Ternary.

## Inspiration
In an age of junk food and unhealthy snacks, people need to be more aware of what they eat. Many are starting to calorie count, but lack a simple way to do this - following through several pages of a mobile app is not ideal, particularly if your hands are full of food! Instead, the solution is a voice-controlled application - just tell Alexa "I just ate a hamburger" and Nutrexa will look up the nutritional content of what you've eaten, make a note of it, and warn you if you're approaching your recommended daily allowance of calories, sodium intake, potassium, etc.

## What it does
Nutrexa tracks your nutrition intake. By speaking to Alexa, you can tell Nutrexa what you've just eaten and ask questions about your food intake that day - "Alexa, how many pizzas did I have today?", "Alexa, what's my calorie level for the day?", "Alexa, am I healthy today?"
Nutrexa warns you when you're eating too much unhealthy food, by tracking when the number of calories / etc. crosses a specified threshold - either by you or by your medical records from your GP.

## How we built it
Using an AWS Lambda instance, we wrote a frontend and a backend for our own Alexa Skill. The Lambda instance runs Python to accept input from the skill and to store it and its nutritional information in the database. The nutritional details come from a web API provided by [Nutritionix](https://developer.nutritionix.com/docs/v2).
Using Lambda, Python, and an Amazon Echo, we wrote the frontend and backend from scratch in just 24 hours.

## Challenges I ran into
We spent a long time troubleshooting a node.js backend and trying to make it communicate with our dynamoDB database. After spending five hours trying to fix this issue, we decided to can node.js and rewrote our application in Python.

## Accomplishments that I'm proud of
At the start, neither of us knew anything about using AWS; we had never used anything Alexa-related, nor had we worked with DynamoDB. One of us didn't know Python, either - so we are very proud of creating a polished product with new technologies while learning how to use them on the fly.

## What we learned
We now understand AWS Lambda instances, non-relational databases (i.e. dynamoDB) and the Alexa skills creation process.

## What's next for Nutrexa
We'd like to future integrate Nutrexa with NHS data - this way Nutrexa can have more information about an individual user's needs. For example, a diabetic person could have a much lower sugar threshold, and this would be pulled from their medical records (with their permission) and incorporated into the app.
