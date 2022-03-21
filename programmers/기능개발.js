/**
 * 2020.12.31
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

////////////////////
//  다른 사람의 풀이  //
////////////////////
function solution(progresses, speeds) {
  const days = progresses.map((p, i) => Math.ceil((100 - p[i]) / speeds[i]));

  const answer = [0];
  let maxDay = days[0];
  for (let i = 0, j = 0; i < days.length; i += 1) {
    if (days[i] <= maxDay) {
      answer[j] += 1;
    } else {
      maxDay = days[i];
      answer[++j] = 1;
    }
  }

  return answer;
}

// map활용해서 계산. 하지만 for문이 더 빠르다고한다
// for문에서 i, j선언 후 i는 순회에, j는 맘대로 사용
// 완주하지못한선수처럼 [++j]를 통해서 속성처럼 인덱스를 넣을 수 있다.
