function solution(S) {
  let answer = [];
  for (let i = 0; i < S.length; i++) {
    for (let j = 0; j < S.length; j++) {
      if (i !== j) {
        for (let k = 0; k < S[i].length; k++) {
          if (S[i][k] === S[j][k]) {
            answer.push([i, j, k]);
          }
        }
      }
    }
  }
  if (answer.length !== 0) {
    return answer[0];
  } else {
    return [];
  }
}

console.log(solution(["gr", "sd", "rg"]));
