/**
 * 내 풀이
 */
function solution(dartResult) {
  const bonus = { S: 1, D: 2, T: 3 };
  const option = { undefined: 1, "*": 2, "#": -1 };
  const array = dartResult.match(/[0-9]+[S|D|T][*|#]?/g);
  for (let i = 0; i < array.length; i += 1) {
    const [s, b, o] = array[i].match(/[0-9]+|[A-Z]|[*|#]/g);
    array[i] = Number(s) ** bonus[b] * option[o];
    if (o === "*" && i > 0) array[i - 1] *= 2;
  }
  return array.reduce((acc, cur) => acc + cur, 0);
}
