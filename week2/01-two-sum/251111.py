class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        map = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in map:
                answer.append(map[num])
                answer.append(i)
            else:
                map[target - num] = i

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
