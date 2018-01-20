var AWS = require("aws-sdk");

var docClient = new AWS.DynamoDB.DocumentClient();

console.log("Adding item in the Databse, table Food_Items");

var returnValue = false;

module.exports = {

  checkItemExistence: function(foodItem) {
    
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

      docClient.query(params, function(err, data) {
          if (err) {
              console.error("Unable to query.");
          } 
          else {
              console.log("Query succeeded.");
              if (data.Items.length == 0)
              {
                returnValue = false;
              }
              else
              {
                returnValue = true;
              }
          }
      });
      console.log("We are getting inside checkItemExistence method");
      return returnValue;
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
    docClient.put(params, function(err, data) {
       if (err) {
           console.error("Unable to add food", foodItem.name);
       } else {
           console.log("PutItem succeeded:", foodItem.name);
       }
    });
    
    console.log("We are getting inside addItemToDB method");

  }

};


