function solution(n, words) {
  const set = new Set();
  let wrong = 0;
  for (let i = 0; i < words.length; i++) {
    const isCorrectWord =
      set.has(words[i]) ||
      (i > 0 && words[i - 1][words[i - 1].length - 1] !== words[i][0]);
    if (isCorrectWord) {
      wrong = i;
      const person = (wrong + 1) % n || n;
      const time = Math.ceil((wrong + 1) / n);
      return [person, time];
    }
    set.add(words[i]);
  }
  return [0, 0];
}
