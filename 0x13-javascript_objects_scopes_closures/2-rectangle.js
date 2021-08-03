#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    /* edge cases */
    if (w < 1 || h < 1) { return; }
    if (w === undefined || h === undefined) { return; }

    /* initialize values */
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
