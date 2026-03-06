var twoSum = function (nums, target) {
  const memo = {};
  const answer = [];

  nums.forEach((num, index) => {
    if (memo[target - num] === undefined) {
      memo[num] = index;
    } else {
      answer.push(memo[target - num]);
      answer.push(index);
    }
  });

  return answer;
};
