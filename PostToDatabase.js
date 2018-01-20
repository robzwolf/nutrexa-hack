var AWS = require("aws-sdk");

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Adding item in the Databse, table Food_Items");

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
        TableName: "Food_Items",
        Item: {
            "Identifier":  foodItem.name,
            "Sodium": (Math.floor(Math.random() * (100 - 20 + 1)) + 20),
            "Potasium":  (Math.floor(Math.random() * (250 - 120 + 1)) + 120)
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
};
