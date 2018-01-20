var AWS = require("aws-sdk");

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Checking item in the Databse, table Food_Items");

module.exports = {

    getItemInformation: function(foodItem, callback){
        var params = {
            TableName: "Food_Items",
            Key:{
                "Identifier": foodItem.name
            }
        };

        docClient.get(params, function(err, data) {
            if (err) {
                console.log("Unable to read item.");
            } else {
                console.log("GetItem succeeded.");
                callback(data);
            }
        });
    }

};
    