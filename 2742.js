let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let answer = "";

for (let i = input[0]; i > 0; i--) {
  // let numbers = input[i].split(" ");
  // answer += Number(numbers[0]) + Number(numbers[1]) + "\n";
  answer += Number(i) + "\n";
}

console.log(answer);