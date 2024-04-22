#!/usr/bin/node

const argOne = parseInt(process.argv[2]);
const argTwo = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(argOne, argTwo);
