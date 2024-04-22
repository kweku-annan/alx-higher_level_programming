#!/usr/bin/node
// Prints arguments passed to it

const args = process.argv;
const concatString = `${args[2]} is ${args[3]}`;
console.log(concatString);
