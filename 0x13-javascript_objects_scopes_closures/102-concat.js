#!/usr/bin/node
// Concats 2 files

const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Lesser number of arguments');
} else {
  const args = process.argv.slice(2);
  const fileA = args[0];
  const fileB = args[1];
  const newFile = args[2];

  fs.readFile(fileA, 'utf8', (err, dataA) => {
	if (err) {
	  console.log(err);
	  return;
	}
	fs.readFile(fileB, 'utf8', (err, dataB) => {
	  if (err) {
		console.log(err);
		return;
	  }
	  const newData = dataA + dataB;
	  fs.writeFile(newFile, newData, 'utf8', (err) => {
		if (err) {
		  console.log(err);
		  return;
		}
	  });
	});
  });
}
