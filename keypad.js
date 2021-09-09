function solution(numbers, hand) {
  const keypad = {
    1: [0, 3],
    2: [1, 3],
    3: [2, 3],
    4: [0, 2],
    5: [1, 2],
    6: [2, 2],
    7: [0, 1],
    8: [1, 1],
    9: [2, 1],
    "*": [0, 0],
    0: [1, 0],
    "#": [2, 0],
  };

  let answer = "";

  //처음 손가락 위치
  let leftFinger = "*";
  let rightFinger = "#";

  for (let i = 0; i < numbers.length; i++) {
    let num = numbers[i];

    if (num % 3 === 1) {
      answer += "L";
      leftFinger = num;
    } else if (num % 3 === 0) {
      answer += "R";
      rightFinger = num;
    } else {
      answer += getDistance(keypad, num, hand, leftFinger, rightFinger);
      answer[answer.length - 1] === "L"
        ? (leftFinger = num)
        : (rightFinger = num);
    }
  }

  return answer;
}

//거리 계산
function getDistance(keypad, num, hand, leftFinger, rightFinger) {
  const handed = hand === "left" ? "L" : "R";
  const left =
    Math.abs(keypad[num][0] - keypad[leftFinger][0]) +
    Math.abs(keypad[num][1] - keypad[leftFinger][1]);
  const right =
    Math.abs(keypad[num][0] - keypad[rightFinger][0]) +
    Math.abs(keypad[num][1] - keypad[rightFinger][1]);
  if (left === right) return handed;

  return left < right ? "L" : "R";
}

console.log(solution(	[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"));

//"LLRLLRLLRL"