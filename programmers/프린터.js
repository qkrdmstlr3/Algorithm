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

////////////////////
//  다른 사람의 풀이  //
////////////////////
function solution(priorities, location) {
  var list = priorities.map((t, i) => ({
    my: i === location,
    val: t,
  }));
  var count = 0;
  while (true) {
    var cur = list.splice(0, 1)[0];
    if (list.some((t) => t.val > cur.val)) {
      list.push(cur);
    } else {
      count++;
      if (cur.my) return count;
    }
  }
}

// some 함수를 사용함으로써 리스트에 최대숫자를 찾아내는 방법을 사용 -> 좀 더 깔끔하게 구현할 수  있다.
