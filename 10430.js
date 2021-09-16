const fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

var A = parseInt(input[0]);
var B = parseInt(input[1]);
var C = parseInt(input[2]);

// var A = 5;
// var B = 8;
// var C = 4;

console.log((A + B) % C);
console.log(((A % C) + (B % C)) % C);
console.log((A * B) % C);
console.log(((A % C) * (B % C)) % C);
