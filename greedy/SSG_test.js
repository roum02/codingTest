function solution(v) {
  var answer = [[]];
  var x = 0;
  var y = 0;

  function Answer(a, b) {
    if (a !== x) {
      //answer.push(a);
      console.log(a);
    }
    if (b !== y) {
      //answer.push(b);
      console.log(b);
    }

    for (let i = 0; i < v.length; i++) {
      for (let j = 0; j < v.length; j++) {
        if (i !== j && v[i][0] == v[j][0]) {
          x = v[i][0];
        }
        if (i !== j && v[i][1] == v[j][1]) {
          y = v[i][1];
        }
      }
    }
    console.log("x", x);
    console.log("y", y);
    v.find(Answer(v[i][0], v[i][1]));
  }

  //for (let i = 0; i < v.length; i++) {}

  return answer;
}

console.log(
  solution([
    [1, 4],
    [3, 4],
    [3, 10],
  ])
);
