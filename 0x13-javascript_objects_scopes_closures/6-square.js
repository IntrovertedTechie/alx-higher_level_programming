#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c = 'X') {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
