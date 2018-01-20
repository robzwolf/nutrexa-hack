var AWS = require("aws-sdk");

AWS.config.update({
    region: "eu-west-1",
    endpoint: "http://localhost:8000"
});

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Checking item in the Databse, table Food_Items");

var table = Food_Items;

var data_to_return = {};

function getItemInformation(foodItem){
    var params = {
        TableName: table,
        Key:{
            "Item": foodItem.name
        }
    };    

    docClient.get(params, function(err, data) {
        if (err) {
            console.error("Unable to read item.");
        } else {
            data_to_return = data;
            console.log("GetItem succeeded.");
        }
    });

    return data_to_return;
};