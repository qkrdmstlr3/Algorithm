function solution(priorities, location) {
  let maxNum = Math.max(...priorities);
  let count = 1;
  while (true) {
    const num = priorities.shift();
    if (num !== maxNum) priorities.push(num);
    else if (location === 0) break;
    else {
      count += 1;
      maxNum = Math.max(...priorities);
    }
    location = location === 0 ? priorities.length - 1 : location - 1;
  }
  return count;
}
