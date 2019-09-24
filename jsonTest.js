// Let's attempt to play around with json data imported in from .json file
// filename in question will be searchRates.json
// written by plscks
// Is this a test?
// It has to be.....
const fs = require('fs');
let jsonData = require('./searchRates.json');
jsonData = convertKeysToLowerCase(jsonData);


function getNames(items) {
  var itemNames = [];
  for (var itemName in items) {
    itemNames.push(itemName);
  }
  return itemNames.sort()
}

function sortResults(input) {
  var sortable = [];
  for (var location in input) {
    sortable.push([location, input[location]]);
  }

  var sortedItems = sortable.sort(function(a, b) {
    return b[1] - a[1];
  });

  return sortedItems
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

function itemsStartWith(masterList, letter) {
  var letterList = [];
  for (i = 0; i < masterList.length; ++i) {
    if (masterList[i].startsWith(letter)) {
      letterList.push(masterList[i]);
    }
  }
  return letterList
}


/*
////////////////////
// EASY TEST CODE //
////////////////////
// The section below is for quick and easy
// testing without readline tracebacks that
// aren't helpful. Keep commented unless testing

// INPUTS //
var item = 'rock';
var letterToList = 'p';
var sortedItems = getNames(jsonData);

// CHECK IF INPUT IN LIST
console.log(!sortedItems.includes(item));
if (!sortedItems.includes(item)) {
  console.log(item + ' not found in database check for a spelling error?');
  return;
}

// LIST ITEMS THAT CAN BE QUERIED
var itemsStartingWith = itemsStartWith(sortedItems, letterToList);
console.log('           ITEMS THAT CAN BE QUERIED');
console.log('+-----------------------------------------------+');
for (i = 0; i < itemsStartingWith.length; ++i) console.log('       ' + itemsStartingWith[i]);

//DISPLAY RESULTS
var itemData = jsonData[item.toLowerCase()];
var sorted = sortResults(itemData);
console.log('');
console.log('');
console.log('Information for ' + item);
console.log('Percent to Find        Location');
console.log('+----------------------------------------------+');
for (var i = 0; i < sorted.length; ++i) {
  var percent = sorted[i][1];
  if (percent < 1) percent = percent.toFixed(3);
  else percent = percent.toPrecision(4)
  console.log(percent + ' -------------- ' + sorted[i][0]);
}
*/

//////////////////////////////////
// Below is interactive version //
//////////////////////////////////
// If using this, make sure the
// test code above is commented out.

const query = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

var sortedItems = getNames(jsonData);

query.question(`What letter does the item start with? : `, (item) => {
  console.log(!sortedItems.includes(item));
  if (!sortedItems.includes(item)) {
    console.log(item + ' not found in database check for a spelling error?');
    return;
  }
  var itemsStartingWith = itemsStartWith(sortedItems, letterToList);
  console.log('           ITEMS THAT CAN BE QUERIED');
  console.log('+-----------------------------------------------+');
  for (i = 0; i < itemsStartingWith.length; ++i) console.log('       ' + itemsStartingWith[i]);
  query.close();
})

query.question(`What item are you searching for? : `, (item) => {
  var itemData = jsonData[item.toLowerCase()];
  var sorted = sortResults(itemData);
  console.log(!sortedItems.includes(item));
  if (!sortedItems.includes(item)) {
    console.log(item + ' not found in database check for a spelling error?');
    return;
  }
  console.log('');
  console.log('');
  console.log('Information for ' + item);
  console.log('Percent to Find        Location');
  console.log('+----------------------------------------------+');
  for (var i = 0; i < sorted.length; ++i) {
    var percent = sorted[i][1];
    if (percent < 1) percent = percent.toFixed(3);
    else percent = percent.toPrecision(4)
    console.log(percent + ' -------------- ' + sorted[i][0]);
  }
  query.close();
})
