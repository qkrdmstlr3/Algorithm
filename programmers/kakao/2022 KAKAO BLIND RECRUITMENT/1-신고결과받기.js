/**
 * 내 풀이
 */
function solution(id_list, report, k) {
  const user = {};
  const result = {};
  id_list.forEach((id) => {
    user[id] = new Set();
    result[id] = 0;
  });
  report.forEach((r) => {
    const [first, second] = r.split(" ");
    user[second].add(first);
  });

  id_list.forEach((id) => {
    if (user[id].size >= k) {
      Array.from(user[id]).forEach((user) => (result[user] += 1));
    }
  });
  return Object.values(result);
}

/**
 * 다른 사람 풀이
 */
function solution(id_list, report, k) {
  const reports = Array.from(new Set(report)).map((r) => r.split(" "));
  const counts = {};
  const good = {};

  reports.forEach(([_, second]) => {
    counts[second] = counts[second] + 1 || 1;
  });
  reports.forEach(([first, second]) => {
    if (counts[second] >= k) {
      good[first] = good[first] + 1 || 1;
    }
  });

  return id_list.map((id) => good[id] || 0);
}

/**
 * 차이
 * 1. Set을 report배열에 한 번만 적용하였다
 * 2. Set을 처음에 한 번 사용함으로써 reports를 두번 forEach로 돌 수 있다.
 * 3. || 연산자를 최대한 활용하여 이중 루프가 돌지 않는다.
 */
