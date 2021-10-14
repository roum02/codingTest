let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let answer = "";

while (True) {
  let numbers = input[i].split(" ");
  if (Number(numbers[0]) + Number(numbers[1]) !== 0) {
    answer += Number(numbers[0]) + Number(numbers[1]) + "\n";
  } else {
    break;
  }
}
