var AWS = require("aws-sdk");

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Checking item in the Databse, table Food_Items");

var data_to_return = {};

function getItemInformation(foodItem){
    var params = {
        TableName: "Food_Items",
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

    while(data_to_return == {}) {}

    return data_to_return;
};