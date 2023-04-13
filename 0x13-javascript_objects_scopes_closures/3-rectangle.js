#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
      // print() {
      //     let X;
      //     let i;
      //     for(let i = 0; i < this.height; i++){
      //         let wi = ""
      //         wi += X
      //         console.log(wi)

    //     }
    //     for (let j = 0; j < this.width; i++){
    //         console.log(X)
    }
  }
};
