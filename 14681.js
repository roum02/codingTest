const fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

var a = Number(input[0]);
var b = Number(input[1]);

// var a = 9;
// var b = -13;

function Quadrant(a, b) {
  return a > 0 && b > 0 ? 1 : a < 0 && b > 0 ? 2 : a < 0 && b < 0 ? 3 : 4;
}

console.log(Quadrant(a, b));
