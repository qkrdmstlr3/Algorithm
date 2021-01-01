function solution(operations) {
  const queue = [];
  operations.forEach((operation) => {
    if (operation.includes("I ")) {
      queue.push(Number(operation.replace("I ", "")));
    } else if (operation.includes("D -1")) {
      const minIndex = queue.indexOf(Math.min(...queue));
      queue.splice(minIndex, 1);
    } else {
      const maxIndex = queue.indexOf(Math.max(...queue));
      queue.splice(maxIndex, 1);
    }
  });
  if (!queue.length) return [0, 0];
  const max = Math.max(...queue);
  const min = Math.min(...queue);
  return [max, min];
}
