/**
 * 내 풀이
 */
const getDis = (first, second) =>
  Math.abs(first[0] - second[0]) + Math.abs(first[1] - second[1]);
function solution(numbers, hand) {
  const keypad = [
    [3, 1],
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
  ];
  let answer = "";
  let left = [3, 0];
  let right = [3, 2];

  numbers.forEach((n) => {
    if (n % 3 === 1) {
      left = keypad[n];
      answer += "L";
    } else if (n && !(n % 3)) {
      right = keypad[n];
      answer += "R";
    } else {
      const leftDistance = getDis(left, keypad[n]);
      const rightDistance = getDis(right, keypad[n]);
      if (
        leftDistance > rightDistance ||
        (leftDistance === rightDistance && hand === "right")
      ) {
        answer += "R";
        right = keypad[n];
      } else if (
        leftDistance < rightDistance ||
        (leftDistance === rightDistance && hand === "left")
      ) {
        answer += "L";
        left = keypad[n];
      }
    }
  });
  return answer;
}

/**
 * 다른 사람 풀이
 */
function solution(numbers, hand) {
  hand = hand[0] === "r" ? "R" : "L"; // 사용하는 손 대문자로 변경
  let position = [1, 4, 4, 4, 3, 3, 3, 2, 2, 2]; // 각 숫자들의 row위치
  let h = { L: [1, 1], R: [1, 1] }; // 0이랑 같은 위치
  return numbers
    .map((x) => {
      if (/[147]/.test(x)) {
        h.L = [position[x], 1];
        return "L";
      }
      if (/[369]/.test(x)) {
        h.R = [position[x], 1];
        return "R";
      }
      let distL = Math.abs(position[x] - h.L[0]) + h.L[1];
      let distR = Math.abs(position[x] - h.R[0]) + h.R[1];
      if (distL === distR) {
        h[hand] = [position[x], 0];
        return hand;
      }
      if (distL < distR) {
        h.L = [position[x], 0];
        return "L";
      }
      h.R = [position[x], 0];
      return "R";
    })
    .join("");
}

/**
 * 차이
 * 위치 정보를 일차원 배열만을 이용하였다.
 * 거리를 일차원 배열만으로 해결할 수 있다는 것이 핵심이다!! (가로거리는 무시해도 된다)
 * reduce함수 사용하면 좋을 것 같다
 */
