#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const results = JSON.parse(body).results;
  for (const result of results) {
    if (result.characters.includes(characterUrl)) {
      count += 1;
    }
  }
  console.log(count);
});
