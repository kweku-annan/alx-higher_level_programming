#!/usr/bin/node
const baseRectangle = require('./4-rectangle');

class Square extends baseRectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
