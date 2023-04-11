#!/usr/bin/node
function factorial(a) {
    if (isNaN(a)) {
      return 1;
    } else if (a <= 1) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
  
  const num = parseInt(process.argv[2]);
  
  console.log(factorial(num));


// function factorial (a) {
//   let total = 1;
//   for (let i = 1; i < a; i++) {
//     total *= a;
//     a -= 1;
//   }
//   return total;
// return a * factorial(a - 1);
// }

// const n = Number(process.argv[2]);

// if (isNaN(n)) {
//   console.log(1);
// } else {
//   console.log(factorial(n));
// }


  