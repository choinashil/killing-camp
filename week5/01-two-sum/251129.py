class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            else:
                num_map[num] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0,1]
    print(solution.twoSum([3, 2, 4], 6))  # [1,2]
    print(solution.twoSum([3, 3,], 6))  # [0,1]
