function solution(people, limit) {
  let answer = 0;
  people = people.sort((a, b) => a - b);
  while (people.length) {
    const personA = people.pop();
    if (personA + people[0] <= limit) {
      people.shift();
    }
    answer += 1;
  }
  return answer;
}
