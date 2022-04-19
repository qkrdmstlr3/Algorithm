/**
 * 내 풀이
 */
function solution(s) {
  const mapping = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  mapping.forEach(
    (item, index) => (s = s.replace(new RegExp(item, "g"), index))
  );
  return Number(s);
}

/**
 * 다른 사람 풀이
 */
function solution(s) {
  let numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  var answer = s;

  for (let i = 0; i < numbers.length; i++) {
    let arr = answer.split(numbers[i]);
    answer = arr.join(i);
  }

  return Number(answer);
}
/**
 * 차이
 * 1. split과 join을 사용해서 정규식을 대체하였다.
 * 특정 문자열을 다른것으로 대체할 때는 split + join을 사용해보자
 */
