/**
 * 내 풀이
 */
function solution(N, stages) {
  const result = new Array(N)
    .fill(0)
    .map(
      (_, i) =>
        stages.filter((s) => i + 1 === s).length /
        stages.filter((s) => s >= i + 1).length
    );

  return Array.from(Array(result.length).keys())
    .sort((a, b) => (result[a] > result[b] ? -1 : (result[b] < result[a]) | 0))
    .map((key) => key + 1);
}

/**
 * 다른 사람 풀이
 */
function solution(N, stages) {
  const result = new Array(N)
    .fill(0)
    .map((_, i) => [
      i + 1,
      stages.filter((s) => i + 1 === s).length /
        stages.filter((s) => s >= i + 1).length,
    ]);

  result.sort((a, b) => b[1] - a[1]);
  return result.map((x) => x[0]);
}

/**
 * 차이
 * index를 담은 result sort를 통해서 이후에 반복문 한 번을 돌지 않고 해결할 수 있다.
 */
