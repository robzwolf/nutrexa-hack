var AWS = require("aws-sdk");

AWS.config.update({
  region: "eu-west-1"
});

var docClient = new AWS.DynamoDB.DocumentClient();

var params = {
    TableName: 'Food_Items',
    Key: {
        "Identifier": "hamburger"
    }
};

console.log("Adding item in the Databse, table Food_Items");

module.exports = {

  checkItemExistence: function(foodItem, callbackWhenTrue, callbackWhenFalse) {

      console.log("Checking item exists for ", foodItem.name);

      docClient.get(params, function(err, data) {
          console.log("Query callback");
          if (err) {
              console.log("Unable to query.", err);
              callbackWhenFalse();
          } 
          else {
              console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
              callbackWhenTrue();
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


