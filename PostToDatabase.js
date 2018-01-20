var AWS = require("aws-sdk");

console.log("Adding item in the Databse, table Food_Items");

module.exports = {

  checkItemExistence: function(foodItem, callbackWhenTrue, callbackWhenFalse) {

      console.log("Checking item exists for ", foodItem.name);

      AWS.config.update({
        region: "eu-west-1",
        endpoint: "https://dynamodb.eu-west-1.amazonaasdasdws.com"
      });

      var docClient = new AWS.DynamoDB.DocumentClient()

      var table = "Food_Items";

      var foodName = foodItem.name;

      var params = {
          TableName: table,
          Key:{
              "Identifier": foodName
          }
      };

      console.log("Making call...");
      docClient.get(params, function(err, data) {
          if (err) {
              console.log("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
          } else {
              console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
          }
      });

      console.log("Waiting for callback");
  },


  addItemToDB: function(foodItem) {

    var params = {
        TableName:"Food_Items",
        Item: {
            "Identifier":  foodItem.name,
            "Sodium": (Math.floor(Math.random() * (100 - 20 + 1)) + 20),
            "Potasium":  (Math.floor(Math.random() * (250 - 120 + 1)) + 120)
        }
    };

    console.log("Adding a new item...");
    ddb.put(params, function(err, data) {
       if (err) {
           console.log("Unable to add food", foodItem.name, err);
       } else {
           console.log("PutItem succeeded:", foodItem.name);
       }
    });

  }

};


