/**
 * 내 풀이
 */
function stableString(t) {
  return ![...t].reduce((acc, s) => acc + (s === "(" ? 1 : -1), 0);
}

function correctString(t) {
  console.log(t);
  while (t.includes("()")) t = t.split("()").join("");
  return !t.length;
}

function changeDirection(t) {
  const a = 1;
  console.log(a);
  return [...t].map((s) => (s === "(" ? ")" : "(")).join("");
}

function solution(p) {
  if (!p.length) return "";
  let i = 2;
  while (!stableString(p.slice(0, i))) i += 2;
  let u = p.slice(0, i);
  let v = p.slice(i);
  if (correctString(u)) return u + solution(v);
  else
    return "(" + solution(v) + ")" + changeDirection(u.slice(1, u.length - 1));
}

/**
 * 다른 사람 풀이
 */
function reverse(str) {
  return str
    .slice(1, str.length - 1)
    .split("")
    .map((c) => (c === "(" ? ")" : "("))
    .join("");
}

function solution(p) {
  if (p.length < 1) return "";

  let balance = 0;
  let pivot = 0;
  do {
    balance += p[pivot++] === "(" ? 1 : -1;
  } while (balance !== 0);

  const u = p.slice(0, pivot);
  const v = solution(p.slice(pivot, p.length));

  if (u[0] === "(" && u[u.length - 1] == ")") return u + v;
  else return "(" + v + ")" + reverse(u);
}

/**
 * 차이
 * do while문을 이용해서 stableString함수를 대체
 * correctString을 51번줄에서 검사하는 방식
 *  > 위에서 균형잡힌것에서 검사를 일차적으로 해주기 때문에, 앞 뒤만 확인해주면 훨씬 멋진 코드를 구현할 수 있다
 *
 * => 좀만 더 노력해보자!
 */
