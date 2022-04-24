/**
 * 내 풀이 1
 */
function solution(r) {
  const a = [];
  const me = { Enter: "님이 들어왔습니다.", Leave: "님이 나갔습니다." };

  return a.map(
    ([i, m]) => a[`id${i}`] + me[m],
    r.forEach((r) => {
      const [s, i, n] = r.split(" ");
      if (s !== "Change") a.push([i, s]);
      if (n) a[`id${i}`] = n;
    })
  );
}

/**
 * 내 풀이 2
 */
function solution(r) {
  const a = [];
  const me = { Enter: "님이 들어왔습니다.", Leave: "님이 나갔습니다." };

  return a.map(
    ([i, m]) => a[`id${i}`] + me[m],
    r.forEach((r) => {
      const [s, i, n] = r.split(" ");
      if (s !== "Change") a.push([i, s]);
      if (n) a[`id${i}`] = n;
    })
  );
}

/**
 * 다른 사람 풀이
 */
function solution(record) {
  const userInfo = {};
  const action = [];
  const stateMapping = {
    Enter: "님이 들어왔습니다.",
    Leave: "님이 나갔습니다.",
  };

  record.forEach((v) => {
    const [state, id, nick] = v.split(" ");

    if (state !== "Change") {
      action.push([state, id]);
    }

    if (nick) {
      userInfo[id] = nick;
    }
  });

  return action.map(([state, uid]) => {
    return `${userInfo[uid]}${stateMapping[state]}`;
  });
}

/**
 * 차이
 * 이번 코드는 내가 더 재밌게 풀었다고 생각한다.
 * 배열(객체의 일종인) a를 사용하여 다른 사람 풀이에서의 userInfo객체의 사용을 없앴다
 */
