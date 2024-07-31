#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const inputText = process.argv[3];

fs.writeFile(filePath, inputText, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
