/**
 * map을 쓰면 한번에 결과를 리턴 가능
 */

function solution(array, commands) {
  return commands.map((command) => {
    const [start, end, num] = command;

    const sortedArray = array.slice(start - 1, end).sort((a, b) => a - b);
    return sortedArray[num - 1];
  });
}
