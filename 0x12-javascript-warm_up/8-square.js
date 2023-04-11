#!/usr/bin/node
const { argv } = require('process');
let i;
const x = argv[2];
const convertedNum = Number(x);
if (isNaN(convertedNum)) {
  console.log('Missing size');
} else {
  for (i = 0; i < convertedNum; i++) {
    let row = '';

    for (let j = 0; j < convertedNum; j++) {
      row += 'X';
    }

    console.log(row);
  }
}
