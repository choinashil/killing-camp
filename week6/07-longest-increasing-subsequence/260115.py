class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(solution.lengthOfLIS([0, 1, 0, 5, 2, 3]))  # 4
    print(solution.lengthOfLIS([0, 1, 0, 5, 1, 3]))  # 3
    print(solution.lengthOfLIS([0, 1, 3, 4, 2, 3, 4, 5]))  # 6
    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
