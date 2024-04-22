#!/usr/bin/node

const nFactorial = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(nFactorial));
