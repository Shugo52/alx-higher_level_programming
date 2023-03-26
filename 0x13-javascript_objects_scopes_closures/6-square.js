#!/usr/bin/node
const Nsquare = require('./5-square.js');

class Square extends Nsquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
}

module.exports = Square;
