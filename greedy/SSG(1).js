function solution(p) {
  var answer = 0;

  const operatorFunctions = {
    "*": (o1, o2) => {
      return o1 * o2;
    },
    "/": (o1, o2) => {
      return o1 / o2;
    },
    "+": (o1, o2) => {
      return o1 + o2;
    },
    "-": (o1, o2) => {
      return o1 - o2;
    },
  };

  const stringPostfix = p.join();

  const arrayPostfix = stringPostfix.split(",");

  const arrayCalcStack = [];

  for (let i = 0; i < arrayPostfix.length; i++) {
    if (!isNaN(arrayPostfix[i])) {
      arrayCalcStack.push(parseFloat(arrayPostfix[i]));
    } else {
      const operator = arrayPostfix[i];

      const operand2 = arrayCalcStack.pop();
      const operand1 = arrayCalcStack.pop();

      const operateResult = operatorFunctions[operator](operand1, operand2);

      arrayCalcStack.push(operateResult);
    }
  }

  answer = arrayCalcStack.pop();

  return answer;
}

console.log(solution(["12", "2", "5", "+", "*", "9", "3", "/", "-"]));
console.log(solution(["1", "1", "+", "1", "1", "+", "*"]));
