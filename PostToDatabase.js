var AWS = require("aws-sdk");

console.log("Adding item in the Databse, table Food_Items");

module.exports = {

  docClient: new AWS.DynamoDB.DocumentClient(),

  checkItemExistence: function(foodItem, callbackWhenTrue, callbackWhenFalse) {
    
      var params = {
          TableName : "Food_Items",
          KeyConditionExpression: "#id = :name",
          ExpressionAttributeNames:{
              "#id": "Identifier"
          },
          ExpressionAttributeValues: {
              ":name":foodItem.name
          }
      };

      console.log("Checking item exists");

      module.exports.docClient.query(params, function(err, data) {
          if (err) {
              console.log("Unable to query.");
          } 
          else {
              console.log("Query succeeded.");
              if (data.Items.length == 0)
              {
                callbackWhenFalse();
              }
              else
              {
                callbackWhenTrue();
              }
          }
      });
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
    module.exports.docClient.put(params, function(err, data) {
       if (err) {
           console.log("Unable to add food", foodItem.name);
       } else {
           console.log("PutItem succeeded:", foodItem.name);
       }
    });

  }

};


