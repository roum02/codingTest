function solution(A) {
  let set = new Set(A);
  let setArr = [...set];
  setArr = setArr.sort();

  for (let i = 0; i < setArr.length; i++) {
    if (setArr[i] < 0) {
      setArr[i] = 0;
    }
  }

  let min = Math.min.apply(null, setArr);

  console.log(min);
}

console.log(solution([-1, 1, 3, 6, 4, 1, 2]));
