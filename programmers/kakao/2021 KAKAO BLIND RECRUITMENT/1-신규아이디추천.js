/**
 * 내 풀이
 */
function solution(new_id) {
  const sixth = (
    new_id
      .toLowerCase() // first
      .replace(/[^\w-_.]/g, "") // second
      .replace(/[.]+/g, ".") // third
      .replace(/^\.|\.$/g, "") || // fourth
    "a"
  ) // fifth
    .slice(0, 15)
    .replace(/\.$/, ""); // sixth

  return sixth.padEnd(3, sixth[sixth.length - 1]);
}

/**
 * 다른 사람 풀이
 */
function solution(new_id) {
  const answer = new_id
    .toLowerCase() // 1
    .replace(/[^\w-_.]/g, "") // 2
    .replace(/\.+/g, ".") // 3
    .replace(/^\.|\.$/g, "") // 4
    .replace(/^$/, "a") // 5
    .slice(0, 15)
    .replace(/\.$/, ""); // 6
  const len = answer.length;
  return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}

/**
 * 차이
 * 1. /^$/ 구문을 사용해 체이닝이 끊기지 않았다
 */
