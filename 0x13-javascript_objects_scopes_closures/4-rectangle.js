#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
    return (this.width, this.height);
  }

  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
    return (this.width, this.height);
  }
}

module.exports = Rectangle;
