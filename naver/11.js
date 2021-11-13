function solution(phone_numbers, phone_owners, number) {
  if (phone_numbers.indexOf(number) !== -1) {
    return phone_owners[phone_numbers.indexOf(number)];
  } else {
    return number;
  }
  // phone_numbers.indexOf(number) !== -1
  //   ? console.log(phone_owners[phone_numbers.indexOf(number)])
  //   : console.log(number);
}

console.log(
  solution(
    ["234-567-890", "444-444-444", "321-543-234"],
    ["해리", "닉", "마이클"],
    "444-444-444"
  )
);
