let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let a = Number(input[0]);

//let a = 3;
let sum = 0;

for (let i = 1; i <= a; i++) {
  sum = sum + i;
}

console.log(sum);
