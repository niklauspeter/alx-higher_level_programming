#!/usr/bin/node
function factorial (a) {
  let total = 1;
  for (let i = 1; i < a; i++) {
    total *= a;
    a -= 1;
  }
  return total;
}

const a = Number(process.argv[2]);

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
