var AWS = require("aws-sdk");

AWS.config.update({
  region: "eu-west-1"
});

var ddb = new AWS.DynamoDB({apiVersion: '2012-10-08'});

console.log("Adding item in the Databse, table Food_Items");

module.exports = {

  checkItemExistence: function(foodItem, callbackWhenTrue, callbackWhenFalse) {

      var params = {
        ExpressionAttributeValues: {
            ':s' : {S: foodItem.name}
           },
         ProjectionExpression: 'Identifier',
         KeyConditionExpression: 'Identifier = :s',
         TableName: 'Food_Items'
        };

      console.log("Checking item exists for ", foodItem.name);

      ddb.query(params, function(err, data) {
          console.log("Query callback");
          if (err) {
              console.log("Unable to query.", err);
          } 
          else {
              console.log("Query succeeded.");
              if (data.Items.length == 0)
              {
                callbackWhenFalse();}
              else
              
              {
                callbackWhenTrue();
              }
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


