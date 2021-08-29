// 로또의 최고 순위와 최저 순위

function solution(lottos, win_nums) {
  var answer = [];

  //배열 안에 중복값이 있는지 여부 함수
  function isDuplicate(arr) {
    const isDup = arr.some(function (x) {
      if (x !== 0) {
        var result = arr.indexOf(x) !== arr.lastIndexOf(x);
      }
      return result;
    });
    return isDup;
  }

  // lottos는 길이가 6인 정수 배열
  // lottos의 모든 원소는 0이상 45이하인 정수
  // win_nums는 길이 6인 정수 배열
  // win_nums의 모든 원소는 1이상 45이하인 정수
  if (
    lottos.length == 6 &&
    lottos.every(function (x) {
      return x >= 0;
    }) &&
    lottos.every(function (x) {
      return x <= 45;
    }) &&
    lottos.every(function (x) {
      return Number.isInteger(x);
    }) &&
    win_nums.length == 6 &&
    win_nums.every(function (x) {
      return x >= 0;
    }) &&
    win_nums.every(function (x) {
      return x <= 45;
    }) &&
    win_nums.every(function (x) {
      return Number.isInteger(x);
    })
  ) {
    // 0을 제외한 다른 숫자는 lottos에 2개 이상 담겨있지 않음
    // win_nums에는 같은 숫자가 2개 이상 담겨있지 않음
    if (!isDuplicate(lottos) && !isDuplicate(win_nums)) {
      // 두 배열 간 교집합 찾기
      const inter = lottos.filter((x) => win_nums.includes(x));

      // 배열 속 0 개수 세기
      const count = lottos.filter((y) => 0 === y).length;

      // min, max 일치 개수 구하기
      // const max = inter.length + count;
      const min = inter.length;

      // 등수로 환산
      if (min == 6) {
        var min_rank = 1;
      } else if (min == 5) {
        var min_rank = 2;
      } else if (min == 4) {
        var min_rank = 3;
      } else if (min == 3) {
        var min_rank = 4;
      } else if (min == 2) {
        var min_rank = 5;
      } else {
        var min_rank = 6;
      }

      // 모든 배열이 일치할 경우
      if (count == 6) {
        var max_rank = 1;
      } else {
        var max_rank = min_rank - count;
      }

      answer.push(max_rank);
      answer.push(min_rank);
      console.log(min_rank);
    }
  }

  return answer;
}

console.log(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]));
