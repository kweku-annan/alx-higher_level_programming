#!/usr/bin/node
// Imports a dictionary of occurences by user id and computes a dictionary of user ids by occurence.

const dict = require('./101-data').dict;
const newDict = {};

// Creating a Set of unique values
const uniqueValues = new Set(Object.values(dict));

uniqueValues.forEach(value => {
  newDict[value] = Object.keys(dict).filter(
    key => dict[key] === value).map(String);
});
console.log(newDict);
