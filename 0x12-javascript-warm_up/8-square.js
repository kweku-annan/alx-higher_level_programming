#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  const character = 'X'.repeat(squareSize);
  for (let i = 0; i < squareSize; i++) {
    console.log(`${character}`);
  }
}
