function solution(S, C) {
  let sum = 0;

  for (let i = 0; i < S.length; i++) {
    if (S[i] === S[i + 1]) {
      sum += C[i];
    }
  }

  return sum;
}

console.log(solution("ababa", [10, 5, 10, 5, 10]));
