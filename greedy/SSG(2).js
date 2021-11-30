function solution(data) {
  var answer = "";
  let pattern = [];
  let index = 0;
  let firstIndex = data.indexOf(data[0]);
  pattern.push(firstIndex);

  while (firstIndex != -1) {
    firstIndex = data.indexOf(data[0], firstIndex + 1);
    if (firstIndex !== -1 && data[firstIndex + 1] == data[1]) {
      pattern.push(firstIndex);
    }
  }
  if (pattern.length === 1) {
    if (data[data.length - 1] !== data[0]) {
      answer = data[0];
    } else {
      answer = data[1];
    }
  } else {
    index = data.length % (pattern[1] - pattern[0]);
    answer = data[index];
  }

  return answer;
}

//console.log(solution(["LU", "M", "RD", "LU", "M", "RD", "LU"]));
console.log(solution(["M", "RD", "LD", "M", "M"]));
