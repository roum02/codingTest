let input = require("fs").readFileSync("dev/stdin").toString();

let x = Number(input[0]);

for (i = 1; i <= 9; i++) {
  console.log(`${x} * ${i} = ${x * i}`);
}
