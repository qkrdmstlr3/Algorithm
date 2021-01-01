let answer = 0;

function dfs(numbers, index, sum, target) {
  if (index === numbers.length) {
    if (sum === target) {
      answer += 1;
    }
    return;
  }
  dfs(numbers, index + 1, sum + numbers[index], target);
  dfs(numbers, index + 1, sum - numbers[index], target);
}

function solution(numbers, target) {
  dfs(numbers, 0, 0, target);
  return answer;
}
