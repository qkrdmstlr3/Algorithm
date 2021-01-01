function solution(n, a, b) {
  let answer = 0;
  while (a !== b) {
    a = Math.round(a / 2);
    b = Math.round(b / 2);
    answer += 1;
  }

  return answer;
}
