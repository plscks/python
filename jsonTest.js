// Let's attempt to play around with json data imported in from .json file
// filename in question will be searchRates.json
// written by plscks
// Is this a test?
// It has to be.....
const fs = require('fs');
let jsonData = require('./searchRates.json');
jsonData = convertKeysToLowerCase(jsonData);

for (var exKey in jsonData) {
  console.log("Item name: " + exKey);
}

function convertKeysToLowerCase(obj) {
    var output = {};
    for (i in obj) {
        if (Object.prototype.toString.apply(obj[i]) === '[object Object]') {
           output[i.toLowerCase()] = convertKeysToLowerCase(obj[i]);
        }else if(Object.prototype.toString.apply(obj[i]) === '[object Array]'){
            output[i.toLowerCase()]=[];
             output[i.toLowerCase()].push(convertKeysToLowerCase(obj[i][0]));
        } else {
            output[i.toLowerCase()] = obj[i];
        }
    }
    return output;
};

const query = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

query.question(`What item are you searching for? : `, (item) => {
  var itemData = jsonData[item.toLowerCase()];
  console.log(itemData);
  query.close();
})
