#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const results = JSON.parse(body).results;
  for (const result of results) {
    const characters = result.characters;
    for (const character of characters) {
      const characterId = character.split('/')[5];
      if (characterId === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
