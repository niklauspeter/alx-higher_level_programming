#!/usr/bin/node
const { argv } = require('process');
const convertedNum = Number(argv[2]);
if (isNaN(convertedNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertedNum}`);
}

// this works too

// if (/^\d+$/.test(arg)) {
//   console.log(`My number: ${parseInt(arg)}`);
// } else {
//   console.log("Not a number");
// }
