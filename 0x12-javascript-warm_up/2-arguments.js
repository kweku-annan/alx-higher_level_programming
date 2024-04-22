#!/usr/bin/node
const { argv } = require('node:process');

const numberOfArgs = argv.length;

if (numberOfArgs <= 2) {
  console.log('No argument');
} else if (numberOfArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
