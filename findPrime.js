// 완전탐색 알고리즘

function solution(numbers) {
  let answer = [];
  let num = numbers.split("").map((x) => Number(x));

  for (let i = 0; i < num.length; i++) {
    if (num[i] < 2) {
    } else {
      for (let k = 2; k < num[i]; k++) {
        if (num[i] % k === 0) {
        }
      }
      answer.push(num[i]);
    }

    for (let j = 0; j < num.length; j++) {
      if (i !== j) {
        if (Number(String(num[i]) + String(num[j])) < 2) {
        } else {
          for (let k = 2; k < Number(String(num[i]) + String(num[j])); k++) {
            if (Number(String(num[i]) + String(num[j])) % k === 0) {
            }
          }
          answer.push(Number(String(num[i]) + String(num[j])));
        }
      }
    }
  }

  return answer;
}

console.log(solution("011"));
