function solution(new_id) {
  var answer = "";

  new_id = new_id.toLowerCase();
  new_id = new_id.replace(/[^a-z0-9-_.]/g, "");
  new_id = new_id.replace("..", ".");
  new_id = new_id.replace(/^\./, "");
  new_id = new_id.replace(/\.$/, "");
  if (new_id == "") {
    new_id = new_id + "a";
  }
  if (new_id.length >= 16) {
    new_id = new_id.substring(0, 15);
  }
  new_id = new_id.replace(/\.$/, "");
  if (new_id.length <= 2) {
    let last = new_id.charAt(new_id.length - 1);
    while (new_id.length < 3) {
      new_id = new_id + last;
      console.log(new_id);
    }
  }

  // new_id.some(i => ["-","_","."].includes(i))
  answer = new_id;

  return answer;
}

console.log(solution("...!@BaT#*..y.abcdefghijklm"));
