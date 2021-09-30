let input = require("fs").readFileSync("dev/stdin").toString().split(" ");

let x = Number(input[0]); // Hour
let y = Number(input[1]); // Minute

function Ago(x, y) {
  return y >= 45
    ? x + " " + (y - 45)
    : x > 0
    ? x - 1 + " " + (60 - (45 - y))
    : 23 + " " + (60 - (45 - y));
}

console.log(Ago(x, y));
