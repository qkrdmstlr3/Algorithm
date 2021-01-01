const set = new Set();

function isDecimal(num) {
  if (num === 1 || num === 0) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function permutation(numbers, selectNumber) {
  const result = [];
  if (selectNumber === 1) return numbers;

  numbers.forEach((number, index) => {
    const rest = [...numbers];
    rest.splice(index, 1);
    const results = permutation(rest, selectNumber - 1);
    result.push(...results.map((result) => number + result));
  });

  return result;
}

function addSet(array) {
  array.forEach((a) => {
    set.add(a);
  });
}

function solution(numbers) {
  for (let i = 1; i <= numbers.length; i++) {
    const results = permutation(numbers.split(""), i);
    addSet(results.map((result) => Number(result)));
  }
  return Array.from(set).reduce((acc, cur) => {
    if (isDecimal(cur)) {
      return (acc += 1);
    }
    return acc;
  }, 0);
}
