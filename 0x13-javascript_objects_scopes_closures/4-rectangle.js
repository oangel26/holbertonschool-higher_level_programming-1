#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    this.width = width;
    this.height = height;
    this.cell = 'X';
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log(this.cell.repeat(this.width));
    }
  }

  rotate () {
    const swap = this.height;
    this.height = this.width;
    this.width = swap;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
