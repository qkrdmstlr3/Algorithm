/**
 * 베스트 풀이법
 * https://programmers.co.kr/learn/courses/30/lessons/42586/solution_groups?language=javascript&type=all
 */
function solution(progresses, speeds) {
  const answer = [];

  while (progresses.length) {
    let count = 0;
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }

    while (progresses[0] >= 100) {
      count += 1;
      progresses.shift();
      speeds.shift();
    }

    if (count) {
      answer.push(count);
    }
  }

  return answer;
}
