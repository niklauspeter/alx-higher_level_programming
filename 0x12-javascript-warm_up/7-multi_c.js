#!/usr/bin/node
const { argv } = require('process');
let i;
const x = argv[2];
const convertedNum = Number(x);
if (isNaN(convertedNum)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < convertedNum; i++) { console.log('C is fun'); }
}
