/**
 * 내 풀이
 */
function getCombinations(valuesArray, store, course) {
  const slent = Math.pow(2, valuesArray.length);

  for (let i = 0; i < slent; i++) {
    const temp = [];
    for (let j = 0; j < valuesArray.length; j++) {
      if (i & Math.pow(2, j)) temp.push(valuesArray[j]);
    }
    if (course.includes(temp.length)) {
      const text = temp.sort().join("");
      if (store[temp.length][text] !== undefined) store[temp.length][text] += 1;
      else store[temp.length][text] = 1;
    }
  }
}

function solution(orders, course) {
  const store = {};
  const result = [];
  course.forEach((c) => (store[c] = {}));
  orders.forEach((order) => getCombinations(order, store, course));
  Object.values(store).forEach((menus) => {
    menus = Object.entries(menus).sort((a, b) => b[1] - a[1]);
    menus.forEach((menu) => {
      if (menu[1] >= 2 && menu[1] === menus[0][1]) result.push(menu[0]);
    });
  });

  return result.sort();
}

/**
 * 다른 사람 풀이
 */
function solution(orders, course) {
  const ordered = {};
  const candidates = {};
  const maxNum = Array(10 + 1).fill(0);
  const createSet = (arr, start, len, foods) => {
    if (len === 0) {
      ordered[foods] = (ordered[foods] || 0) + 1;
      if (ordered[foods] > 1) candidates[foods] = ordered[foods];
      maxNum[foods.length] = Math.max(maxNum[foods.length], ordered[foods]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      createSet(arr, i + 1, len - 1, foods + arr[i]);
    }
  };

  orders.forEach((od) => {
    // arr.sort는 기본적으로 사전식 배열
    const sorted = od.split("").sort();
    // 주문한 음식을 사전순으로 배열해서 문자열을 만든다.
    // course에 있는 길이만 만들면 된다.
    course.forEach((len) => {
      createSet(sorted, 0, len, "");
    });
  });

  const launched = Object.keys(candidates).filter(
    (food) => maxNum[food.length] === candidates[food]
  );

  return launched.sort();
}

/**
 * 차이
 */
