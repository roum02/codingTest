function solution(ip_addresses, registered_list, banned_list) {
  var answer = [];
  for (let i = 0; i < ip_addresses.length; i++) {
    answer.push(1);
  }

  //서버등록: 0
  let registered_string = registered_list.join();
  answer[ip_addresses.indexOf(registered_string)] = 0;
  //차단: 3
  //console.log(answer);
  let banned_string = banned_list.join();
  answer[ip_addresses.indexOf(banned_string)] = 3;

  for (let i = 0; i < answer.length; i++) {
    if (answer[i] == 1) {
      let temp_list = ip_addresses[i].split(".");
      for (let j = 0; j < temp_list.length; j++) {
        if (0 <= temp_list[j] <= 255) {
          if (temp_list[j].startsWith(0) && temp_list[i].length == 1) {
            answer[i] = 2;
          }
        }
      }
    }
  }

  return answer;
}

console.log(
  solution(
    ["115.86.56.15", "123.12.2.1.", "...", "255.255.1.256"],
    ["115.86.56.15"],
    ["123.12.2.1"]
  )
);
