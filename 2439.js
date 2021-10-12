let input = require("fs").readFileSync("/dev/stdin").toString();
let num = Number(input);

let list = new Array(num).fill(" ");

for (let i = num - 1; i >= 0; i--) {
  list[i] = "*";
  console.log(list.join(""));
}
