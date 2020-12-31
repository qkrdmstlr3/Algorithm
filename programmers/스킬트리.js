/**
 * 베스트 풀이법
 * https://programmers.co.kr/learn/courses/30/lessons/49993/solution_groups?language=javascript
 */
function solution(skill, skill_trees) {
  return skill_trees.reduce((acc, skills) => {
    const skillText = skills.split("").reduce((acc, cur) => {
      if (skill.includes(cur)) {
        return (acc += cur);
      }
      return acc;
    }, "");

    if (skill.indexOf(skillText) === 0 || !skillText.length) {
      return (acc += 1);
    }
    return acc;
  }, 0);
}
