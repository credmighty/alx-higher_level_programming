#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let a = 0; a < this.width; a++) {
      x += 'X';
    }
    for (let b = 0; b < this.height; b++) {
      console.log(x);
    }
  }
}
module.exports = Rectangle;
