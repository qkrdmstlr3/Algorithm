/**
 * 내 풀이
 */
function chunkString(str, length) {
  return str.match(new RegExp(".{1," + length + "}", "g"));
}

function parseArray(array) {
  return array.reduce((acc, text) => {
    if (!acc.length) acc.push([text, 1]);
    else if (acc[acc.length - 1][0] === text) acc[acc.length - 1][1] += 1;
    else acc.push([text, 1]);
    return acc;
  }, []);
}

function getLength(arr) {
  return arr.reduce(
    (acc, [key, value]) =>
      acc + key.length + (value === 1 ? 0 : String(value).length),
    0
  );
}

function solution(s) {
  let result = s.length;
  for (let i = 1; i <= s.length / 2; i += 1) {
    const parsedArray = parseArray(chunkString(s, i));
    const length = getLength(parsedArray);
    if (length < result) result = length;
  }
  return result;
  // const range = [...Array(s.length)].map((_, i) => i + 1);
  // return Math.min(...range.map((i) => getLength(parseArray(chunkString(s, i)))));
}

/**
 * 다른 사람 풀이
 */
const solution = (s) => {
  const range = [...Array(s.length)].map((_, i) => i + 1); // 1~s길이까지 배열 생성
  return Math.min(...range.map((i) => compress(s, i).length)); // 길이별로 자른 문자열들의 결과 길이 비교
};

const compress = (s, n) => {
  const make = ([a, l, c]) => `${a}${c > 1 ? c : ""}${l}`;
  return make(
    chunk(s, n).reduce(
      ([a, l, c], e) => (e === l ? [a, l, c + 1] : [make([a, l, c]), e, 1]),
      ["", "", 0]
    )
  );
};

const chunk = (s, n) =>
  s.length <= n ? [s] : [s.slice(0, n), ...chunk(s.slice(n), n)];

/**
 * 차이
 * Math.min과 map, range를 이용해서 for문 없이 구현
 */
