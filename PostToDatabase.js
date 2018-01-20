var AWS = require("aws-sdk");

AWS.config.update({
    region: "eu-west-1",
    endpoint: "http://localhost:8000"
});

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Adding item in the Databse, table Food_Items");

var table = Food_Items;

function checkItemExistence(foodItem) {
	if (foodItem.name) {
		//read from db and check existance
		return true;
	}
	else
		return false;
}


function addItemToDB(foodItem) {
    var params = {
        TableName:table,
        Item: {
            "Identifier":  foodItem.name,
            "Sodium": 20,
            "Potasium":  120
        }
    };

	console.log("Adding a new item...");
    docClient.put(params, function(err, data) {
       if (err) {
           console.error("Unable to add food", foodItem.name);
       } else {
           console.log("PutItem succeeded:", foodItem.name);
       }
    });
});
