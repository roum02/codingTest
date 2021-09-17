const fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

var a = parseInt(input[0]);
var b = parseInt(input[1]);

// var a = 472;
// var b = 385;
var sum = 0;

for (let i = 1; i < 4; i++) {
  var value = Number(b.toString().substr(-i, 1)) * a;
  console.log(value);
  sum = sum + value * 10 ** (i - 1);
}

console.log(sum);
