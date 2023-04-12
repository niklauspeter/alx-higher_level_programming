#!/usr/bin/node
const argNum = Number(process.argv.length);
const args = process.argv;
const arr = [];

if (Number(argNum) < 3) {
  console.log(0);
} else if (Number(argNum) === 3) {
  console.log(0);
} else {
  for (let i = 2; i < (argNum); i++) {
    arr.push(args[i]);
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}

// this can also work
// const args = process.argv.slice(2).map(arg => parseInt(arg));

// if (args.length < 2) {
//   console.log(0);
// } else {
//   const sortedArgs = args.sort((a, b) => b - a);
//   console.log(sortedArgs[1]);
// }
