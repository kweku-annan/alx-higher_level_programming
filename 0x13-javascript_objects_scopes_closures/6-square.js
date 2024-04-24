#!/usr/bin/node
const baseSquare = require('./5-square');

class Square extends baseSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined || c === null) { c = 'X'; }
    const character = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(character);
    }
  }

  double () {
    this.size *= 2;
  }
}

module.exports = Square;
