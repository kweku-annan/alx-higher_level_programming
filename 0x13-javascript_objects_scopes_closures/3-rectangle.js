#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const character = 'X'.repeat(this.width);
    let i = 0;
    while (i < this.height) {
      console.log(character);
      i++;
    }
  }
}

module.exports = Rectangle;
