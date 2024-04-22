#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let newArray = args.slice(2);
  newArray = newArray.sort((a, b) => b - a);
  console.log(newArray[1]);
}
