function solution(N) {
  if (N > 100000000) {
    return -1;
  } else {
    let number = [];
    for (let i = 0; i < String(N).length; i++) {
      number.push(String(N)[i]);
    }
    number = number.map(Number);

    number.sort(function (a, b) {
      return b - a;
    });

    return Number(number.join(""));
  }
}

console.log(solution(1991));
