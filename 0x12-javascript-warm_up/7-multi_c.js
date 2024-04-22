#!/usr/bin/node

const xTimes = parseInt(process.argv[2]);
if (isNaN(xTimes)) {
  console.log('Missing number of occurances');
} else {
  let i = 0;
  while (i < xTimes) {
    console.log('C is fun');
    i++;
  }
}
