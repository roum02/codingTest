function solution(numbers, hand) {
  var answer = String(numbers).replace(/1|4|7/g, "L").replace(/3|6|9/g, "R");
  return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
