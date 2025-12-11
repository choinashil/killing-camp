class Solution:
    def rob(self, nums):
        for i in range(2, len(nums)):
            if i == 2:
                nums[i] = nums[i] + nums[i - 2]
            else:
                nums[i] = max(nums[i - 2] + nums[i], nums[i - 3] + nums[i])

        if len(nums) == 1:
            return nums[-1]
        else:
            return max(nums[-1], nums[-2])

# 참조


class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))  # 4
    print(solution.rob([2, 7, 9, 3, 1]))  # 12
    print(solution.rob([3, 1, 1, 5, 1, 1, 1, 1, 1]))  # 10
    print(solution.rob([2, 1, 1, 2]))  # 4
