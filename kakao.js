function solution(id_list, report, k) {
  var answer = [];

  const warnedID = {};
  report.forEach((x) => {
    warnedID[x.split(" ", 2)[1]] = (warnedID[x.split(" ", 2)[1]] || 0) + 1;
  });
  console.log(warnedID);

  return answer;
}

console.log(
  solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2
  )
);
