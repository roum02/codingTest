let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let answer = "";

for (let i = 1; i <= input[0]; i++) {
  answer += "*".repeat(i) + "\n";
}

console.log(answer);
