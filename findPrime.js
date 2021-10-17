//완전탐색 알고리즘

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

    // for (let j = 0; j < num.length; j++) {
    //   if (i !== j) {
    //     if (Number(String(num[i]) + String(num[j])) < 2) {
    //     } else {
    //       for (let k = 2; k < Number(String(num[i]) + String(num[j])); k++) {
    //         if (Number(String(num[i]) + String(num[j])) % k === 0) {
    //         }
    //       }
    //       answer.push(Number(String(num[i]) + String(num[j])));
    //     }
    //   }
    // }
  }

  return answer;
}

console.log(solution("011"));

function getNumbeOfCases(numbers) {
  // 중복을 막기 위해서
  const result = new Set();

  // 재귀 함수를 통해 만든다.
  const temp = (currFix, eachArr) => {
    for (let i = 0; i < eachArr.length; i++) {
      const tempEachArr = [...eachArr];
      const tempCurrFixVal = tempEachArr.splice(i, 1)[0];
      const tempCurrFix = currFix + tempCurrFixVal;
      result.add(Number(tempCurrFix));
      if (tempEachArr.length > 0) temp(tempCurrFix, tempEachArr);
    }
  };

  // 시작
  for (let i = 0; i < numbers.length; i++) {
    let target = numbers[i];
    result.add(Number(target));

    const eachArr = [...numbers];
    eachArr.splice(i, 1);

    temp(target, eachArr);
  }

  return new Array(...result);
}
