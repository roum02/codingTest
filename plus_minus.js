// function solution(absolutes, signs) {
//   var answer = absolutes.map((x, index) => {
//     return signs[index] ? x : -x;
//   });
//   return answer.reduce((a, b) => a + b);
// }

function solution(absolutes, signs) {
  var result = absolutes.reduce((acc, val, i) => {
    console.log(acc, val, i);
    return acc + val * (signs[i] ? 1 : -1), 0;
  });
}

console.log(solution([4, 7, 12], [true, false, true]));
