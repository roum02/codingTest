function solution(absolutes, signs) {
  var answer = absolutes.map((x, index) => {
    return signs[index] ? x : -x;
  });
  return answer.reduce((a, b) => a + b);
}

console.log(solution([4, 7, 12], [true, false, true]));
