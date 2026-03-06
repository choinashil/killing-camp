class Solution:
    def twoSum(self, nums, target):
        memo = {}
        answer = []

        for index, num in enumerate(nums):
            if target - num in memo:
                answer.append(memo[target - num])
                answer.append(index)
                break
            else:
                memo[num] = index

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
