function solution(A, B) {
  let mul = A * B;
  let binary = mul.toString(2);

  let count = 0;
  let search = "1";
  let pos = binary.indexOf(search);
  while (pos !== -1) {
    count++;
    pos = binary.indexOf(search, pos + 1);
  }
  return count;
}

console.log(solution(3, 7));
