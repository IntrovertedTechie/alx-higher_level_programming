#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0) || !h || !w) {
      // Create an empty object if width or height is not positive
      toString();
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
