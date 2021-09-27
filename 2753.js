const fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

var a = Number(input[0]);
// var b = Number(input[1]);

// var a = 2000;

function isLeapYear(a) {
  return a % 4 == 0 && (a % 100 !== 0 || a % 400 == 0) ? 1 : 0;
}

console.log(isLeapYear(a));
