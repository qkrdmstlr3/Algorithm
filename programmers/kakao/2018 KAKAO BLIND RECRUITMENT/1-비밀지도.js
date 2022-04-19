/**
 * 내 풀이
 */
function solution(n, arr1, arr2) {
  const answer = new Array(n).fill("");
  arr1 = arr1.map((i) => i.toString(2).padStart(n, "0").split(""));
  arr2 = arr2.map((i) => i.toString(2).padStart(n, "0").split(""));

  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      answer[i] += arr1[i][j] | arr2[i][j] ? "#" : " ";
    }
  }

  return answer;
}

/**
 * 다른 사람 풀이
 */
var solution = (n, a, b) =>
  a.map((a, i) =>
    (a | b[i]).toString(2).padStart(n, 0).replace(/0/g, " ").replace(/1/g, "#")
  );

/**
 * 차이
 * 10진수끼리 or연산을 해도 2진수의 결과가 나올 수 있다.
 * 문자열 배열에도 정규식을 쓸 수 있다
 */
