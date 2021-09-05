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

  //거리 계산
  function getDistance() {}
  // var answer = String(numbers).replace(/1|4|7/g, "L").replace(/3|6|9/g, "R");
  return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
