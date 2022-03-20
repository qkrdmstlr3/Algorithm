function solution01(participant, completion) {
  participant = participant.sort();
  completion = completion.sort();
  for (var i = 0; i < participant.length; i++) {
    if (participant[i] !== completion[i]) {
      return participant[i];
    }
  }
}

////////////////////
//  다른 사람의 풀이  //
////////////////////
var others = (participant, completion) => {
  return participant.find(
    (name) => !completion[name]--,
    completion.forEach(
      (name) => (completion[name] = (completion[name] | 0) + 1)
    )
  );
};

const parti = ["mislav", "stanko", "mislav", "ana"];
const comple = ["stanko", "ana", "mislav"];
others(parti, comple);

// ['cake', 'ball', 'sauce', 'cake', cake: 2, ball: 1, sauce: 1] 그냥 이렇게 쓰면 오류가 발생한다.
// 1. find의 두 번째 인자가 먼저 실행된다 > completion이 먼저 가공된다
// 2. OR 을 사용해서, "만약 completion[name]이 존재하면, 그 값에 +1 을 한 것", 이고, "존재 안하면, 0 + 1 (즉 1이죠)"으로 정의해라. 등장한 이름 횟수만큼 증가시킨다.
// 3. completion[name]이란? completion은 배열인데 가능?
//   3-1. 배열은 사실 객체이다.
//   3-2. forEach로 completion을 돌리면 cake:2 등은 나오지 않는데, 속성이라서 그렇다. forEach는 배열의 요소에 대해서만 루프를 돈다.
//        근래에 추가된 forEach는 이런 속성에 대해 인정하지 않는다는 신념이 들어간 것 같다. 그냥 for문으로 돌릴 경우 배열의 요소와 속성이 같이 나온다.
// 4. 1인 것은 완주자 목록에 있음으로 제외한다
