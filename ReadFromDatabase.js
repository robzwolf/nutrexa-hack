var AWS = require("aws-sdk");

AWS.config.update({
    region: "eu-west-1",
    endpoint: "http://localhost:8000"
});

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Checking item in the Databse, table Food_Items");

var table = Food_Items;


var item_Name = foodItem.name;

var params = {
    TableName: table,
    Key:{
        "Item": identifier,
        "Sodium": sodium,
        "Potasium": potasium
    }
};

docClient.get(params, function(err, data) {
    if (err) {
        console.error("Unable to read item.");
    } else {
        console.log("GetItem succeeded.");
    }
});