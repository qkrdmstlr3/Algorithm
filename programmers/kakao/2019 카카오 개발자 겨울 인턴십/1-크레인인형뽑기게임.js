/**
 * 내 풀이
 */
function solution(board, moves) {
  const basket = [];

  return moves.reduce((acc, cur) => {
    for (let i = 0; i < board.length; i += 1) {
      if (board[i][cur - 1] == 0) continue;
      if (basket[basket.length - 1] !== board[i][cur - 1])
        basket.push(board[i][cur - 1]);
      else {
        acc += 2;
        basket.pop();
      }
      board[i][cur - 1] = 0;
      break;
    }
    return acc;
  }, 0);
}

/**
 * 다른 사람 풀이
 */
const transpose = (matrix) =>
  matrix.reduce(
    (result, row) => row.map((_, i) => [...(result[i] || []), row[i]]),
    []
  );

const solution = (board, moves) => {
  const stacks = transpose(board).map((row) =>
    row.reverse().filter((el) => el !== 0)
  );
  const basket = [];
  let result = 0;

  for (const move of moves) {
    const pop = stacks[move - 1].pop();
    if (!pop) continue;
    if (pop === basket[basket.length - 1]) {
      basket.pop();
      result += 2;
      continue;
    }
    basket.push(pop);
  }

  return result;
};

/**
 * 차이
 * 1. trapnspose함수를 이용해서 보드의 방향을 바꾸었다.
 * [
  [ 0, 0, 0, 0, 0 ],
  [ 0, 0, 1, 0, 3 ],
  [ 0, 2, 5, 0, 1 ],
  [ 4, 2, 4, 4, 2 ],
  [ 3, 5, 1, 3, 1 ]
]
[
  [ 0, 0, 0, 4, 3 ],
  [ 0, 0, 2, 2, 5 ],
  [ 0, 1, 5, 4, 1 ],
  [ 0, 0, 0, 4, 3 ],
  [ 0, 3, 1, 2, 1 ]
]
 */
