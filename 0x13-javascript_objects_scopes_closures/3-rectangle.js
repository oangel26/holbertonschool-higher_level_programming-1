#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    this.width = width;
    this.height = height;
  }

  print () {
    const cell = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(cell.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
