#!/usr/bin/node

const Quar = require('./5-rectangle');
class Square extends Quar {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let a = 0; a < this.height; a++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
